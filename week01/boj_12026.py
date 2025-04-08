
def min_energy_to_link(N, blocks) : 
    dp = [float('inf')] * (N+1) # 최소 에너지 저장 
    dp[1] = 0 # 1번에서 시작
    boj_block  = ['B', 'O', 'J'];

  
    for i in range(0, N):
        next_boj = 0
        if(blocks[i] == 'B'):
            next_boj = 1;
        elif(blocks[i] == 'O'):
            next_boj = 2;
        elif(blocks[i] == 'J'):
            next_boj = 0;

        # i번 블럭에서 뒤에 갈 수 있는 블럭 전부 체크
        for j in range(i + 1, N):
            if blocks[j] == boj_block[next_boj]:
                jump_distance = j - i
                energy = jump_distance * jump_distance
                dp[j+1] = min(dp[j+1], dp[i+1] + energy)

    

    # dp[N] 혹은 도착 못하면 -1
    return dp[N] if dp[N] != float('inf') else -1
            

N = int(input())  
blocks = input().strip()  # BOJ 문자열

print(min_energy_to_link(N, blocks))