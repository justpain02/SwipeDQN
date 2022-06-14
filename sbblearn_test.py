from stable_baselines3 import DQN, PPO
import os
from gym_sbbgames import SBBEnv
import time

models_dir = f"models/{int(time.time())}/"
logdir = f"logs/{int(time.time())}/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

env = SBBEnv()
env.reset()

policy_kwargs = dict(
        net_arch=[128, 54, 54]
    )

model = DQN('MlpPolicy', env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log=logdir)
# model = DQN('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

TIMESTEPS = 100
iters = 0
for iters in range(1, 200):
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"DQN", log_interval=1)
	model.save(f"{models_dir}/{TIMESTEPS*iters}")

