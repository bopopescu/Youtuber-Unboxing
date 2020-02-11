import datetime
from .models import *


#   - kinds = 1 파급력 ( 커뮤니티 언급수(그래프), 뉴스언급수, 조회수 ,구독자 대비 조회수)
def get_influence(youtuber):
    value = len(Community.objects.filter(yno=youtuber.yno)) + len(News.objects.filter(yno=youtuber.yno))
    Stat.objects.create(
        yno=youtuber,
        kinds=1,
        value=value
    )
    return get_score_from_stat(1, value)

#   - kinds = 2 활동 지수 ( 최근 10개 영상 업로드 주기 )
#   음수 값을 만든다. 
def get_activity(youtuber, video_detail_list):
    max_num = min(len(video_detail_list), 10)
    datetime_list = []
    for i in range(max_num):
        datetime_list.append(datetime.datetime.strptime(video_detail_list[i]['regDate'], '%Y-%m-%d'))
    dif_sum = 0
    for i in range(max_num - 1):
        dif_sum += (datetime_list[i] - datetime_list[i+1]).days
    Stat.objects.create(
        yno=youtuber,
        kinds=2,
        value=-dif_sum/max_num
    )
    return get_score_from_stat(2, -dif_sum/max_num)

#   - kinds = 3 구독자 수 성장세 (  )
def get_trend(youtuber, last_month_trend, today_trend):
    value = 0
    if last_month_trend == None:
        value = 0
    else:
        value = (int(today_trend.pointsubscriber) - int(last_month_trend.pointsubscriber))/int(last_month_trend.pointsubscriber)*100
    Stat.objects.create(
        yno=youtuber,
        kinds=3,
        value=value
    )
    return get_score_from_stat(3, float(value))

#   - kinds = 4 조회수 성장세 ( )
def get_views(youtuber, last_month_trend, today_trend):
    value = 0
    if last_month_trend == None:
        value = 0
    else:
        value = int(today_trend.pointview) - int(last_month_trend.pointview)
    Stat.objects.create(
        yno=youtuber,
        kinds=4,
        value=float(value)
    )
    return get_score_from_stat(4, float(value))

#   - 호감도 ( 좋아요 수, 총 영상의 좋아요, 싫어요 비율, 댓글 수 )
def get_charm(video_list):
    good = 0
    bad = 0
    value = 0
    for video in video_list:
        if not video['good'] or video['good'] == None:
            continue
        good += int(video['good'])
        bad += int(video['bad'])
    if good + bad == 0:
        value = 0
    else:
        value = int(good * 100 / (good + bad))
    return value

#   - 등급 
def get_grade(stat_influence, stat_activity, stat_trend, stat_views, stat_charm):
    grade = 'X'

    
    return (stat_influence + stat_activity + stat_trend + stat_views + stat_charm)/5


def get_score_from_stat(kinds, value):
    ability_list = Stat.objects.filter(kinds=kinds).order_by('value')
    n = len(ability_list)
    index = -1
    i = 1
    for ability in ability_list:
        if value == ability.value:
            index = i
            break
        i += 1
    if index == -1:
        print('***** stat에서 %d 종류의 %.2f 값을 찾을 수 없음' % (kinds, value))
    return 100 - int((n-(index))*100/n)


def get_activity2(youtuber, video_detail_list):
    max_num = min(len(video_detail_list), 10)
    datetime_list = []
    k = 0
    for video_detail in video_detail_list:
        datetime_list.append(video_detail.regdate)
        k += 1
        if k == max_num:
            break
        
    dif_sum = 0
    for i in range(max_num - 1):
        dif_sum += (datetime_list[i] - datetime_list[i+1]).days
    Stat.objects.create(
        yno=youtuber,
        kinds=2,
        value=dif_sum/max_num
    )
    print('stat 추가됨')
    return get_score_from_stat(2, dif_sum/max_num)


def get_charm2(video_list):
    good = 0
    bad = 0
    value = 0
    for video in video_list:
        if not video.good or video.good == None:
            continue
        good += int(video.good)
        bad += int(video.bad)
    if good + bad == 0:
        value = 0
    else:
        value = int(good * 100 / (good + bad))
    return value