# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument("sq",type=int)
# args=parser.parse_args()
# print(args.sq**2)

# import argparse
# parser2=argparse.ArgumentParser()
# parser2.add_argument('--fff',action='store_true')
# parser2.add_argument('dodo')
# print(parser2.parse_known_args(['--fff','dodomen','iAm','girl']))


# Concepts of sub-command
import argparse
parserr=argparse.ArgumentParser()
subparsers=parserr.add_subparsers()

sub_a=subparsers.add_parser('firstsubcommand')
sub_a.add_argument('f',help='the name of firstsubcommand')

print(parserr.parse_args(['firstsubcommand','d']))
print("OK")
# dest
# import argparse
# parser3=argparse.ArgumentParser()
# subparsers=parser3.add_subparsers(dest="storedName")
# subparser1=subparsers.add_parser('-namefrom_dest')
# subparser2=subparsers.add_parser('Good')
# print(parser3.parse_args(['Good']))



