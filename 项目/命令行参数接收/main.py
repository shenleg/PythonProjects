import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.",
                                     description='help info.')
    parser.add_argument('--domain', type=str, required=True, help='机构代码')
    parser.add_argument('--testcases', type=str, default=2, required=False,
                        help='测试用例')
    args = parser.parse_args()

    print(args)
    print(args.domain)
    print(type(args.testcases), args.testcases)

# python main.py --domain do
# Namespace(domain='do', testcases=2)
# do
# <class 'int'> 2
