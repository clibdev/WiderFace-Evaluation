from scipy.io import loadmat

filename = 'ground_truth/wider_face_val_bbx_gt_v2.txt'

targets = {}
with open('ground_truth/wider_face_val_bbx_gt.txt', 'r') as file:
    for path in file:
        rows = []
        for _ in range(int(file.readline())):
            data = list(map(int, file.readline().split())) + [0] * 3
            rows.append(data)
        targets[path] = rows

easy = loadmat('ground_truth/wider_easy_val.mat')
medium = loadmat('ground_truth/wider_medium_val.mat')
hard = loadmat('ground_truth/wider_hard_val.mat')

gt_list = [easy['gt_list'], medium['gt_list'], hard['gt_list']]

data = ''
for i in range(len(easy['event_list'])):
    for j in range(len(easy['file_list'][i][0])):
        path = easy['event_list'][i][0][0] + '/' + easy['file_list'][i][0][j][0][0] + '.jpg\n'
        for k, gt in enumerate(gt_list):
            for value in gt[i][0][j][0]:
               targets[path][value[0] - 1][k + 10] = 1

data = ''
for path, rows in targets.items():
    data += path + str(len(rows)) + '\n'
    for values in rows:
        data += ' '.join([str(val) for val in values]) + '\n'

with open(filename, 'w') as file:
    file.write(data)
