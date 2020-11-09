from p2pool.bitcoin import networks

PARENT=networks.nets['digibyte']
SHARE_PERIOD=25
CHAIN_LENGTH=24*60*60//10
REAL_CHAIN_LENGTH=24*60*60//10
TARGET_LOOKBEHIND=200
SPREAD=30

#IDENTIFIER='1bfe01eff5ba4e39'.decode('hex') # +1
#PREFIX='1bfe01eff652e4b8'.decode('hex') # +1

IDENTIFIER='83E65D2C81BF6D66'.decode('hex')
PREFIX='83E65D2C81BF6D68'.decode('hex')

P2P_PORT=5024
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=True
WORKER_PORT=5025
BOOTSTRAP_ADDRS='217.72.4.157 217.72.6.241 86.52.128.133 192.168.10.10'.split(' ') # '161.43.201.255 '.split(' ')
ANNOUNCE_CHANNEL='#p2pool'
VERSION_CHECK = lambda v: None if 7170200 <= v else 'DigiByte version too old. Upgrade to 7.17.2 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit', 'reservealgo', 'odo'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000