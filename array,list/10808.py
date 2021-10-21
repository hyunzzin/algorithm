arr = ['a','b','c','d','e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

st = input()
for j in range(len(arr)):
    arr[j] = st.count(arr[j])
    print(arr[j], end=' ')
