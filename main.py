def Policy(actedAction: str) -> int:
  '''
    External policy calculator function that is responsible for policy per action
  '''
    sum = 0
    
    for action in env.ActionSpace:
        
        if actedAction == "Move":
            sum += 25
        elif actedAction == "Talk":
            sum += 15
            
    return sum

def RewardAgent(reward: int, action: str) -> int:
  '''
    Helper function to reward agent based on policy
  '''
    return reward + Policy(action) * 2

class Agent:
    '''
        Agent Class, contains the Reward it is allowed to receive along with rewards receive
    '''

    def __init__(self) -> None:
        self.Reward = 0
        self.RewardReceived = {}

    def act(self, action) -> None:
        self.RewardReceived[action] += RewardAgent(self.Reward, action)
        
class AgentEnv:
    '''
      Agent Environment Class, contains the Action Space to perform and be rewarded for, along with the instantiated Agent 
      in the environment.
    '''
    def __init__(self) -> None:
        self.Acted = {}
        self.ActionSpace = ["Move", "Talk"]
        self.Agent = Agent()

    def record(self) -> None:
        self.Acted["AGENT"] = self.Agent.ActionActed
        self.Acted["ENV"] = self.Acted["AGENT"]
        print(self.Agent.RewardReceived)
  
