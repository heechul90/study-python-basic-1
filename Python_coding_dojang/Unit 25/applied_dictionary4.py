### Unit 25. 딕셔너리 응용하기
## 25.4 딕셔너리 안에서 딕셔너리 사용하기

## 딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}


terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet)
print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8



## 딕셔너리[키][키]
## 딕셔너리[키][키] = 값
print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8