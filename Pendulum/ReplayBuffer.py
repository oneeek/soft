from collections import deque
import numpy as np
import random



class ReplayBuffer():
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = deque()
        self.count = 0

    def buffer_count(self):
        return self.count
        
    def add_buffer(self, state, action, reward, next_state, done):
        new = (state, action, reward, next_state, done)
        if self.count < self.buffer_size:
            self.buffer.append(new)
            self.count += 1
        else:
            self.buffer.popleft()
            self.buffer.append(new)
            
    def sample_batch(self, batch_size):
        if self.count < batch_size:
            batch = random.sample(self.buffer, self.count)
        else:
            batch = random.sample(self.buffer, batch_size)

        states = np.asarray([i[0] for i in batch])
        actions = np.asarray([i[1] for i in batch])
        rewards = np.asarray([i[2] for i in batch])
        next_states = np.asarray([i[3] for i in batch])
        dones = np.asarray([i[4] for i in batch])
        return states, actions, rewards, next_states, dones
