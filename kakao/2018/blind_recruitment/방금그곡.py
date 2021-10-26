def get_between(start, end):
    [sh, sm] = start.split(':')
    [eh, em] = end.split(':')
    return int(eh) * 60 + int(em)  - (int(sh) * 60 + int(sm))

def convert(melody):
    asis = ['C#', 'D#', 'F#', 'G#', 'A#']
    tobe = ['c', 'd', 'f', 'g', 'a']
    for a, b in zip(asis, tobe):
        melody = melody.replace(a,b)
    return melody

def solution(m, musicinfos):
    arr = []
    m = convert(m)
    for musicinfo in musicinfos:
        [start, end, title, melody] = musicinfo.split(',')
        melody = convert(melody)
        play_time = get_between(start, end)
        melody_time = len(melody)
        played_melody = (melody * (play_time // melody_time + 1))[:play_time]
        if m in played_melody:
            arr.append([title, play_time])
    if len(arr) == 0: return '(None)'
    return sorted(arr, key=lambda x: -x[1])[0][0]