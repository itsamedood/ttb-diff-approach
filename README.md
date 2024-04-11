# TTB (Text To Brainf**k)

# What?
> Different approach instead using fancy-pants math to convert text to Brainf**k as done in [BFI](https://github.com/itsamedood/bfi/blob/60453503cda5ab18df10fec4610922be1c9faea8/src/interpreter.py#L99C3-L99C36):
>
> The format produced is near identical to what I used in [Brainless Bot](https://github.com/itsamedood/brainless-bot).
>
> Only real difference is:
>> ```bf
>> Brainless Bot
>> >>++++[<++++++++>-]<..               Space (x2) = 32
>> == VS ==
>> TTBDA
>> >>++++[<++++++++>-]<..                    Space = 32
>> ```
>>
> It can also produce a compact format (`--compact=<int>`) if you don't want the comments.
>> ```bf
>> >+++++[<+++++++>-]<.>>++++[<++++++++>-]<.>>+++++[<
>> +++++++++++++++++>-]<-..>>++++++[<+++++++++++>-]<.
>> >>++++[<++++++++>-]<.>>++++[<++++++++++>-]<.>>++++
>> +[<+++++++++++++++++>-]<-.>>++++++++++[<++++++++++
>> >-]<+.>>++++++++++[<++++++++++++>-]<.>>++++++++++[
>> <+++++++++++>-]<++++++.>>++++[<++++++++>-]<.
>> ```
>
> You can have all the code one 1 line if you want by specifying `compact` as `0`.
>> Check [test/gitignore.bf](test/gitignore.bf) for an example.

---

# Why?
> bored 🤷‍♂️
