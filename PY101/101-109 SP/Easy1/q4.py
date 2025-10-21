length = float(input('Enter the length of the room in meters'))
width = float(input('Enter the width of the room in meters'))


area_in_meters = length * width
area_in_feet = area_in_meters * 10.7639
print(f'area in square meters is: {area_in_meters:.2f}'
      f'area in sqaure feet is: {area_in_feet:.2f}')
