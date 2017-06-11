"""
demonstrating dicts
dict include list include a named tuple
"""
import collections

def load_data():
    '''
    :return:
    '''
    def bin_manipulation(hbin1=None,hbin2=None,hbin3=None,hbin4=None,hbin5=None,
                        hbin6 = None, hbin7 = None):
        '''
        --> result, <-- named tuple of results
        :param hbin1:
        :param hbin2:
        :param hbin3:
        :param hbin4:
        :param hbin5:
        :param hbin6:
        :param hbin7:
        :return:
        '''
        hbins = locals()
        bins = collections.namedtuple('bin', 'Category, result')
        bin_result = []

        for hbin in hbins:
            # key == hbin
            # value == hbins[hbin]
            if hbins[hbin] is not None:
                bin_result.append(bins(hbin,hbins[hbin]))
        return bin_result

    lot = {}

    lot['0/0']= bin_manipulation(hbin1=True, hbin7=False)
    lot['0/1']= bin_manipulation(hbin1=True, hbin5=False)
    lot['0/2']= bin_manipulation(hbin1=True)
    lot['0/3']= bin_manipulation(hbin1=True)
    lot['0/4']= bin_manipulation(hbin1=True)
    lot['0/5']= bin_manipulation(hbin1=True)
    lot['0/6']= bin_manipulation(hbin1=True)
    lot['1/0']= bin_manipulation(hbin1=True)
    lot['1/0']= bin_manipulation(hbin1=True)
    lot['1/1']= bin_manipulation(hbin1=True)
    lot['1/2']= bin_manipulation(hbin1=True)
    lot['1/3']= bin_manipulation(hbin1=True)
    lot['1/4']= bin_manipulation(hbin1=True)
    lot['1/5']= bin_manipulation(hbin1=True)
    lot['1/6']= bin_manipulation(hbin1=True)
    lot['1/7']= bin_manipulation(hbin1=True, hbin7=False)
    lot['1/8']= bin_manipulation(hbin1=True)
    lot['2/1']= bin_manipulation(hbin1=True, hbin4=False)
    lot['2/2']= bin_manipulation(hbin1=True, hbin3=False)
    lot['2/3']= bin_manipulation(hbin1=True)
    lot['2/4']= bin_manipulation(hbin1=True)
    lot['2/5']= bin_manipulation(hbin1=True, hbin7=False)
    lot['2/6']= bin_manipulation(hbin1=True)
    lot['2/7']= bin_manipulation(hbin1=True)
    lot['2/8']= bin_manipulation(hbin1=True)
    lot['2/9']= bin_manipulation(hbin1=True, hbin7=False)

    return lot


if __name__ == '__main__':
    some_lot = load_data()

    for die in some_lot:
        print(die + ' ----', some_lot[die])
