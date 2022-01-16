#!/usr/bin/env python3


import subprocess
import argparse
from subprocess import CalledProcessError, call
from sys import stdout


def argsFunction():
    # subprocess.run(['git', 'add *'])
    # process = subprocess.call(['git', 'init'])           
    # print(process)

    # output = process.stdout
    # output

    parser = argparse.ArgumentParser(description = 'github shortcuts')
    # parser.add_argument('-n', '--name', help="string of name")

    parser.add_argument('-cm', '--commit', help="commits to git, with message")


    parser.add_argument('-cc', '--compareCommits', help="compares the last two commits and pushes them out to ./mypatch.txt, repsond with \'true\'")

    parser.add_argument('--log', help="show (oneline) log of commits, repsond with \'true\'")

    parser.add_argument('-nb', '--newbranch', help="new branch, with new name")
    parser.add_argument('-sb', '--switchbranch', help="use name of branch to switch to")

    parser.add_argument('-allb', '--allbranches', help="show all branhces")

    # parser.add_argument('-opl', '--openlast', help="opens last commit")
    parser.add_argument('-pl', '--pull', help="pulls from clone")
    parser.add_argument('-pu', '--push', help="pushes to repo")
    parser.add_argument('-cl', '--clone', help="clones from repo")




    args = parser.parse_args()

    # print (args.name)

    if(args.commit):
        # print(args.commit)
        commit(args.commit)

    if(args.pull=='true'):
        pull()
    if(args.push=='true'):
        push()
    if(args.clone):
        clone(args.clone)

    # ===================
    if (args.compareCommits == 'true'):
        pullLog()
        pullCommit()
    if(args.log == 'true'):
        log()

    # ===================
    if(args.newbranch):
        branchNew(args.newbranch)
    if(args.switchbranch):
        switchBranch(args.switchbranch)

    if(args.allbranches == 'true'):
        listBranches()

    # if


# ===================
def commit(message):
    message2 = "\""+message+"\""
    try:
        process = subprocess.check_output("git add .", shell=True)
        process = subprocess.check_output("git commit -m "+str(message2), shell=True)
        print('Commited!')
    except CalledProcessError as err:
        print("error: {0}".format(err)) 
        print('Posibility nothing to Commit...')   


# ===================
processLogOut=''
def pullLog():
    global processLogOut
    # processLog = subprocess.run('git log --oneline', capture_output=True )
    # print(processLog.stdout)
    
    processLog = subprocess.check_output('git log --oneline', shell=True)
    print('===only using first two===')
    print (processLog)
    processLogOut = processLog.splitlines()


def pullCommit():
    data = processLogOut
    # data = ['80f1990 (HEAD -> master) second', 'a74c762 first']    
    # firstSpace = data.find(' ')
    # print(data[0:firstSpace])

    # afterBreakLine = data[firstSpace:].find('\n')
    # secondNumber = data[afterBreakLine:]
    firstCommit = data[0][0:data[1].find(' ')]
    secondCommit = data[1][0:data[1].find(' ')]
    print("===\nNEW: " + firstCommit+' '+" OLD: " +secondCommit)

    processLog = subprocess.check_output('git diff '+  firstCommit +' '+ secondCommit + ' > ./mypatch.txt', shell=True)
    print("Exported to ./mypatch.txt\n===")

# ===================
def log():
    process = subprocess.check_output('git log --oneline', shell=True)
    print(process)
# ===================

def branchNew(name):
    process = subprocess.check_output('git checkout -b '+ name , shell=True)
    print(process)

def switchBranch(name):
    process = subprocess.check_output('git checkout ' + name, shell=True)
    print(process)

def listBranches():
    process = subprocess.check_output('git branch -a', shell=True)
    print(process)

def pull():
    process = subprocess.check_output('git pull', shell=True)

def push():
    process = subprocess.check_output('git push', shell=True)

def clone(url):
    process = subprocess.check_output('git clone '+url, shell=True)



if __name__ == "__main__":
    argsFunction()