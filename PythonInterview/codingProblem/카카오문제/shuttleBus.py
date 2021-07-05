'''
셔틀은 9시부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
셔틀이 도착했을 때 도착한 순가에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발.
예를 들어 9시 도착한 셔틀에 자리가 있다면 9시 줄을 선 크루도 탈 수 있다.

timetable : 크루가 대기열에 도착하는 시각 배열 모음
'''

from typing import List

def solution(n: int, t:int, m : int, timetable:List[int]) -> str :
    timetable = [int(time[:2]) * 60 + int(time[3:])
                 for time in timetable]

    timetable.sort()

    current = 9*60

    for _ in range(n):
        for _ in range(m):

            # 대기가 있는 경우 1초 전 도착
            if timetable and (timetable[0] <= current) :
                candidate = timetable.pop(0) - 1 # 마지막의 1초전

            else: # 대기가 없는 경우 정시 도착
                candidate = current

        current += t

    # 분, 초로 다시 변경

    h, m = divmod(candidate, 60)
    return(str(h).zfill(2)+":"+str(m).zfill(2))

