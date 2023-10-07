def is_valid(state):
    m1,c1,b,m2,c2=state
    return 0<=m1<=3 and 0<=c1<=3 and 0<=m2<=3 and 0<=c2<=3 and ((m1==0 or m1>=c1) and (m2==0 or m2>=c2))
def generate_next_states(state):
    m1,c1,b,m2,c2=state
    moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    next_states=[]
    for dm,dc in moves:
        if b==1:
            new_state=(m1-dm,c1-dc,0,m2+dm,c2+dc)
        else:
            new_state=(m1+dm,c1+dc,1,m2-dm,c2-dc)
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states
def solve_bfs(start_state):
    queue=[(start_state,[start_state])]
    while queue:
        current_state,path=queue.pop(0)
        if current_state==(0,0,0,3,3):
            return path
    for next_state in generate_next_states(current_state):
        if next_state not in path:
            queue.append((next_state,path+[next_state]))
    return None
start_state=(3,3,1,0,0)
solution=solve_bfs(start_state)
if solution:
    a=0
    print("solution path:")
    for state in solution:
        m1,c1,b,m2,c2=state
    print(f"{m1}missionaries,{c1}cannibols,{'boat on left'if b==1 else 'boat on right'},{m2}missionaries,{c2}cannibals")
    a=a+1
    print("total cost is:",a)
else:
    print("No Solution found")
        













    
