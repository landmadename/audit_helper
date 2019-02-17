import re
from fuzzywuzzy import fuzz


class course():
    def __init__(self,
                 course_data_filename='classes_data'):
        self.data_dict = {
            'course_name': 0,
            'course_time': 1,
            'teacher_name': 2,
            'place': 3,
            'weekday': 4,
            'year': 5,
            'term': 6,
            'grade': 7,
            'college': 8,
            'major': 9,
            'class': 10
        }
        self.data = self.load_data(course_data_filename)
        self.course_time = \
            [self.format_course_time((i[1], i[4])) for i in self.data]
        self.course_names = list(set([i[0] for i in self.data]))
        self.course_names_for_search = self.process_course_names_for_search()

    def load_data(self, filename):
        import pickle
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        return data

    def process_course_names_for_search(self):
        data = []
        for i in self.course_names:
            data.append(' '.join([ii for ii in i]))
        return data

    def format_course_time(self, data):
        data, weekday = data
        week = []
        week_range = re.findall('(.*?)\(', data)[0]
        week_range = week_range.split(',')
        index = re.findall('\((.*?)\)', data)[0]
        index = index.split(',')
        index = [int(i) for i in index]
        for i in week_range:
            t = re.findall('(\d+)-(\d+)', i)
            if t == []:
                week.append(int(re.findall('\d+', i)[0]))
            else:
                a, b = t[0]
                if '单' in i or '双' in i:
                    week = week + list(range(int(a), int(b) + 1, 2))
                else:
                    week = week + list(range(int(a), int(b) + 1))
        return week, weekday, index

    def groupby(self, data, key_name):
        import itertools
        data.sort(key=lambda x: x[self.data_dict[key_name]])
        data = [(i, list(ii)) for i, ii in
                itertools.groupby(data, lambda x:x[self.data_dict[key_name]])]
        return data

    def get_data_by_course_name(self, name):
        data = [i for i in self.data
                if i[self.data_dict['course_name']] == name]
        data = self.groupby(data, 'teacher_name')
        data_list = []
        for i in data:
            data_list.append({
                'course_name': name,
                'teacher_name': i[0],
                'data': [', '.join([ii[1],
                                    '周' + str(ii[4]),
                                    ii[3],
                                    ii[10],
                                    ii[8]])
                         for ii in i[1]]
            })
        return data_list

    def search(self, kw):
        kw = ' '.join([ii for ii in kw])
        data = [(fuzz.token_set_ratio(i, kw), self.course_names[e]) for e, i in
                enumerate(self.course_names_for_search)]
        data.sort(reverse=True)
        data = [i for i in data if i[0] >= 50]
        return [i[1] for i in data]


cs = course()
