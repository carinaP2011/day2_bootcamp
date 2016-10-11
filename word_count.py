def word_counts(obj):
    the_words={}#we will return this

    for i in obj.split():
        if i in the_words:
            the_words[i]+=1
        else:
            the_words[i]=1

    return the_words


print (word_counts("old fish young fish red fish yellow fish 123 $#@$@#$@#4: 324234 @#$#@$#@$,,,,, "))
