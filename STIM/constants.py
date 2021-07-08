import numpy as np

SUMMARY_FODLER	= 'Summary/'
MODEL_FOLDER	= 'model/'
TRAIN_FOLDER	= 'Train/'
TEST_FOLDER		= 'Test/'
# TEST_FOLDER		= 'Test_large/'

GPU_ID			= 0

INSTANCE_NUM	= 1

RANDOM			= 0
LEAST_CONNECT	= 1
STRATEGIC_START	= 2
START_NODE_STG	= STRATEGIC_START

USE_GPU 		= True
LOW_MEMORY		= True
LOAD 			= True
SAVE_NETWORK	= True
SAVER_INTERVAL	= 5

ALPHA_RL		= 1.0
ALPHA_SUP		= 0.5
LAMBDA			= 1e-2

RL_MODEL		= 0
SUP_MODEL		= 1
ALL_MODEL		= 2
MODEL_TO_TRAIN	= RL_MODEL

GCN				= 0
S2VEC			= 1
S2VEC_NORM		= 2
EMBED_METHOD	= S2VEC_NORM

GREEDY 			= 0
STRATEGIC_AGENT	= 1
NSTEP_QL		= 2
TEMP_DEG_AGENT	= 3
STRATEGY 		= NSTEP_QL
#STRATEGY 		= GREEDY
#STRATEGY 		= STRATEGIC_AGENT
#STRATEGY 		= TEMP_DEG_AGENT

TRAIN 			= 0
TEST			= 1 ## TODO change after train
REAL_NET		= 2
MODE			= TRAIN

if MODE == REAL_NET:
	START_NODE_STG = LEAST_CONNECT

BEST_ACTION		= True
N_THREADS		= 1
STEP_ONE 		= True
DISCOUNT_REWARD	= False

IMMEDIATE_REWARD	= 0
IMMEDIATE_REWARD_NEG= 1
EPISODE_REWARD		= 2
EPISODE_REWARD_NEG	= 3
SPECIAL_REWARD		= 4
HIGH_DIFFUSION		= 5
IMMEDIATE_DISCOUNT	= 6
INFLUENCE			= 7
INFLUENCE_NORM		= 8
REWARD_TYPE 		= INFLUENCE_NORM

DIFUSION_WEIGHT		= 1.0
COUNT_WEIGHT		= 0.5
DEGREE_WEIGHT		= 0.0

USE_LSTM		= True
NODE_RANK		= False
USE_NORMALIZE	= False
LAYERS 			= 2
LSTM_LAYERS_F1	= 2
LSTM_LAYERS_F2	= 3
USE_Q			= False
NORMALIZE_Q		= False
USE_DOUBLE_FLOW	= True

N_ATOM 			= 21
VMIN 			= -0.5
VMAX			= 1.0
DELTA_Z 		= (VMAX - VMIN) / float(N_ATOM - 1)
ATOMS 			= [VMIN + i * DELTA_Z for i in range(N_ATOM)]
#ATOMS 			= np.arange(VMIN, VMAX + DELTA_Z/2, DELTA_Z)
NUM_FEATURES 	= 4
EMBED_SIZE		= 128
LSTM_SIZE_F1	= 64
LSTM_SIZE_F2	= 128
LEARNING_RATE	= 7e-5
MIN_LEARNING_RT	= 1e-6
#LEARNING_RATE	= 1e-4
#MIN_LEARNING_RT	= 5e-5
LR_DECAY 		= 0.999
GAMMA			= 0.7

TIME_LIMIT		= 8
USE_CLASS		= True
CLASS_RANGE		= [0.5, 0.1, 0.0]
N_CLASS 		= len(CLASS_RANGE)
SIGMOID 		= False

BATCH_SIZE		= 8	#128
NORM_CLIP		= 40.0
#*********************
EXPLORATION_RT	= 0.8
MIN_EXP_RT		= 0.3
#*********************
EXP_DECAY		= 0.001

USE_EXP			= True
SCORE_TH		= 0.4
MAX_N_EXP		= 25
EXP_RATE		= 3

DIFUSION_RATE	= 0.002
PCT_MAX_STEPS	= 0.4
MAX_STEPS		= 20#10
MIN_STEPS		= 10#5
PCT_START_NODE	= 0.02
PCT_START_TIME	= 0.5
N_GRAPH_ITERATE	= 2000
MAX_TO_KEEP		= 5

OUT_SIZE		= 1
if USE_CLASS:
	OUT_SIZE 	= N_CLASS

REWARD_NAME		= 'Im'
if REWARD_TYPE == IMMEDIATE_REWARD:
	REWARD_NAME		= 'Im'
elif REWARD_TYPE == IMMEDIATE_REWARD_NEG:
	REWARD_NAME		= 'Im_n'
elif REWARD_TYPE == EPISODE_REWARD:
	REWARD_NAME		= 'Ep'
elif REWARD_TYPE == EPISODE_REWARD_NEG:
	REWARD_NAME		= 'Ep_n'
elif REWARD_TYPE == SPECIAL_REWARD:
	REWARD_NAME		= 'Sp'
elif REWARD_TYPE == HIGH_DIFFUSION:
	REWARD_NAME		= 'Hd'
elif REWARD_TYPE == INFLUENCE:
	REWARD_NAME		= 'In'
elif REWARD_TYPE == INFLUENCE_NORM:
	REWARD_NAME		= 'InNorm_' + str(DIFUSION_WEIGHT) + '_' + str(COUNT_WEIGHT)  + '_' + str(DEGREE_WEIGHT)
else:
	REWARD_NAME		= 'ImR'

TRAIN_NAME		= 'RL'
if MODEL_TO_TRAIN == SUP_MODEL:
	TRAIN_NAME	= 'SUP'
elif MODEL_TO_TRAIN == ALL_MODEL:
	TRAIN_NAME 	= 'ALL'

LAYER_NAME = '2l'
if LAYERS == 1:
	LAYER_NAME = '1l'
elif LAYERS == 3:
	LAYER_NAME = '3l'
elif LAYERS > 3:
	print("Max layers = 3!")
	exit(0)

Q_NAME = 'Qnorm'
if not USE_Q:
	Q_NAME = 'NoQ'
elif not NORMALIZE_Q:
	Q_NAME = 'Q'

DISCOUNT_EXTRA = ''
if not DISCOUNT_REWARD:
	DISCOUNT_EXTRA = '_DIS=' + str(DISCOUNT_REWARD)

FLOW_EXTRA = ''
if USE_DOUBLE_FLOW:
	FLOW_EXTRA = '_2Flow'
if not USE_LSTM:
	FLOW_EXTRA = '_SEQ'

METHOD_NAME = S2VEC_NORM
if EMBED_METHOD == S2VEC:
	METHOD_NAME = 'S2VEC'
elif EMBED_METHOD == S2VEC_NORM:
	METHOD_NAME = 'S2VEC_NORM'

FOLDER 			= '../Graphs/'
SUMMARY_NAME	= 	METHOD_NAME + '_' + Q_NAME + '_VAR_' + LAYER_NAME + '_' + TRAIN_NAME + \
					'_NORM=' + str(USE_NORMALIZE) + '_F=' + str(NUM_FEATURES) + '_M=' + \
					str(MAX_TO_KEEP) + '_Batch=' + str(BATCH_SIZE) + '_R=' + \
					str(int(NODE_RANK)) + '_G=' + \
					str(int(GAMMA*100)) + '_' + REWARD_NAME + '_LAMBDA=' + \
					"{:.0e}".format(LAMBDA) + '_ATOMS=' + str(N_ATOM) + \
					DISCOUNT_EXTRA + '_EXP=' + str(USE_EXP) + FLOW_EXTRA + '_LR=' + \
					"{:.0e}".format(LEARNING_RATE) + '_MinLR=' + "{:.0e}".format(MIN_LEARNING_RT) + \
					str(INSTANCE_NUM)
print("\n\nSUMMARY = ", SUMMARY_NAME, "\n\n")
SUMMARY_INT_SCR	= 10
SUMMARY_INT_LOSS= 10
MODEL_PATH		= MODEL_FOLDER + SUMMARY_NAME + '/'
NO_ACTION 		= -1