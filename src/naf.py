import tensorflow as tf

from .network import Network
from .memory import Network
from .utils import get_timestamp

class NAF(object):
  def __init__(self, env):
    self.env = env
    self.memory = Memory()

    self.pred_network = Network(
      input_shape=env.observation_space.shape,
      action_size=env.action_space.n + 1,
      hidden_dims=[200, 200],
    )
    self.target_network = Network(
      input_shape=env.observation_space.shape,
      action_size=env.action_space.n + 1,
      hidden_dims=[200, 200],
    )
    self.target_network.make_copy_from(self.pred_network)

  def train(self, n_episodes, lr, learn_start, display=False):
    step_op = tf.Variable(0, trainable=False, name='step')
    self.optim = tf.train.AdamOptimizer(lr) \
      .minimize(self.network.loss, global_step=step_op)

    tf.initialize_all_variables().run()
    saver = tf.train.Saver(self.network.variables + [step_op], max_to_keep=30)

    self.env.monitor.start('/tmp/%s-%s' % (self.env.name, get_timestamp())
    for episode in xrange(n_episodes):
      state = env.reset()

      for t in xrange(max_step):
        if display: env.render()

        state_, reward, terminal, _ = env.step(action)
        self.memory.add(state, action, reward, terminal, state_)
        state = state_

        if self.memory.size > learn_start:
          loss = 0

          for iteration in xrange(max_train):
            prestates, actions, rewards, terminals, poststates = memory.sample()

        if terminal: break

    env.monitor.close()
