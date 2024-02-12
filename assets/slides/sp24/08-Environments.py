
def say_hi(name):
    print(f'Hi, {name}')

say_hi = lambda name: print(f'Hi, {name}')

fruits = ["pear", "grape", "KIWI", "APPLE", "melon", "ORANGE", "BANANA"]
sorted(key=lambda x: x.lower())


sorted([5, 4, 3, 2, 1])

# This is the "identity" function
sorted([5, 4, 3, 2, 1], key = lambda x: x)

sorted([1,2,3,4,5], key = lambda x: -x)

sorted([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], key = lambda x:x[0])

sorted([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], key = lambda x:x[1])

sorted([(2,"hi"),(1,"how"),(5,"goes"),(7,"I")], key =lambda x: len(x[1]))

full_names = ['Rebecca Dang', 'Ramya Chitturi', 'Aymeric Barrier', 'Sean Yang', 'Joanna Yoo', 'Amit Sant', 'Michelle Chen', 'John Teng', 'Lukas Chang', 'Anjali Gurajapu', 'Christine Zhang', 'Ethan Yoo', 'Karim Kaylani', 'Mingxiao Wei', 'Michael Ball', 'Sebastian Zhao', 'Hetal Shah']

staff = list(map(lambda w: w.split()[0], full_names))
# staff = ['Anjali', 'Mingxiao', 'Aymeric', 'Karim', 'Ethan', 'Michelle', 'Christine', 'Joanna', 'Lukas', 'John', 'Sebastian', 'Sean', 'Amit', 'Michael', 'Ramya', 'Rebecca', 'Hetal']

sorted(staff)

sorted(staff, key = lambda name: len(name))

# More practice with map / filter / reduce
remove_dupes = lambda result, data: result if data in result else result + [ data ]

from functools import reduce
reduce(remove_dupes, staff, [])

course = {
    'name': 'Comp Structures in Data Science',
    'number': 'C88C',
    'room': '155 Dwinelle Hall'
}

text = 'Once Upon A Time'

counts  = { word : len(word) for word in text.split(' ') }
counts

counts.keys()
counts.values()
counts.items()
# counts['time']
# counts['hello']
counts.get('hello')
