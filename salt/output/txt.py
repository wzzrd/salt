'''
The txt outputter has been developed to make the output from shell
commands on minions appear as they do when the command is executed
on the minion.
'''

# Import python libs
import pprint

def output(data):
    '''
    Output the data in lines, very nice for running commands
    '''
    ret = ''
    if hasattr(data, 'keys'):
        for key in data:
            value = data[key]
            # Don't blow up on non-strings
            try:
                for line in value.split('\n'):
                    ret += '{0}: {1}\n'.format(key, line)
            except AttributeError:
                ret += '{0}: {1}\n'.format(key, value)
    else:
        # For non-dictionary data, just use print
        ret += '{0}\n'.format(pprint.pformat(data))

    return ret

