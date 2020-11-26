using DelimitedFiles

function read_file(file)
    contents = readdlm(file, ' ', Int)
    return contents
end