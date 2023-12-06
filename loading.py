from init import *

xv = np.array(pd.read_csv('testing_data/xv.csv',header=None))
yv = np.array(pd.read_csv('testing_data/yv.csv',header=None))
phi = np.array(pd.read_csv('testing_data/phi.csv',header=None))
step = np.load('testing_data/step.npy')
data = np.load('testing_data/data.npy')
zv_path = 'testing_data/zv.csv'
check = os.path.isfile(zv_path)
if check == True:
    zv = np.array(pd.read_csv('testing_data/zv.csv',header=None))
else:
    zv= []

# print(np.max(zv)-np.min(zv))