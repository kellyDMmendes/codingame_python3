''' Your virus has caused a backdoor to open on the Bobnet network enabling
you to send new instructions in real time.
You decide to take action by stopping Bobnet from communicating on its own
internal network.
Bobnet's network is divided into several smaller networks, in each sub-network
is a Bobnet agent tasked with transferring information by moving from node to
node along links and accessing gateways leading to other sub-networks.
Your mission is to reprogram the virus so it will sever links in such a way
that the Bobnet Agent is unable to access another sub-network thus preventing
information concerning the presence of our virus to reach Bobnet's central
hub. '''
n, l, e = [int(i) for i in input().split()]
EI = 0
link = []

for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    link.append([n1] + [n2])
link.sort()
link.reverse()

exit_gat = []
for i in range(e):
    EI = int(input())
    exit_gat.append(EI)


def next_link(agent):
    ''' Find the next link '''
    j = 0
    while j < len(link):
        for _, ex in enumerate(exit_gat):
            if ex in link[j]:
                if agent in link[j]:
                    result = str(link[j][0]) + " " + str(link[j][1])
                    link.pop(j)
                    return result
        j += 1
    return ""


while True:
    si = int(input())
    CUT = next_link(si)

    if CUT == "":
        CUT = str(link[0][0]) + " " + str(link[0][1])
        link.pop(0)

    print(CUT)
    i = 0
    CUT = ""
    CONTROL = False
