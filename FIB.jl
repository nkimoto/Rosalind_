include("utils/file_handler.jl")

# 多層ディスパッチで使用するInteger型を引数にとるメソッドを定義
function fib(n::Integer, k::Integer)
    # メモ初期化
    d = Dict(zero(n)=>big"1", one(n)=>big"1")
    fib(n, d, k)
end

# 引数が3つの場合は下記の関数に渡される
function fib(n, d, k)
    # メモ内に値があれば返す
    if haskey(d, n)
        return d[n]
    end
    # n-1, n-2項目の値からn項目の値を求める
    result = fib(n-1, d, k) + k * fib(n-2, d, k)
    # メモ化
    d[n] = result
    return result
end

n, k = read_file("data/rosalind_fib.txt")
println(fib(n, k))