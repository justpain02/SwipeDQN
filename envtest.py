from stable_baselines3.common.env_checker import check_env
from gym_sbbgames import SBBEnv


env = SBBEnv()
# It will check your custom environment and output additional warnings if needed
check_env(env)
action = env.action_space.sample()
observation, reward, done, info = env.step(action)
print(observation, reward, done, info)
if done:
    observation = env.reset()