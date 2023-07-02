K = int(input())

for data_set_num in range(K):
    hydra_heads = int(input())
    actions = input()

    for action in actions:
        if action == 'c':
            hydra_heads += 1
        else:
            hydra_heads -= 1
        if hydra_heads == 0:
            break

    print(f"Data Set {data_set_num+1}:")
    print(hydra_heads)
    print()
