# Bean NFT Generator
Do you think NFT are dumb? I do they're a MLM for gullible people. Then I read things like "AI Generated" and claim that because of that they're unique. 99% of them are not unique.

You can edit the `x` and `y` vars in either `defaultbeans()` or `coolbeans()` you can use any parametric equations. I used the lima bean curve because I think is funny.

This is the command to generate cool beans. Thanks to @JohanC on stackoverflow for helping me with this one as well as some other issues I had. `ax.fill(np.r_[x * 1.01, x[::-1] * 0.93], np.r_[y * 1.01, y[::-1] * 0.93],  c=(1, 0.2, 0.5))`

## Commands
`-c or --cool` to generate a cool bean
`-d or --default` to generate the default meme
`-m or --mixed` to generate an equal amount of cool and default beans

`python nft_gen.py -c 3`

`python nft_gen.py -d 6`

`python nft_gen.py -m 9`

## Notes
The algorithm could be fixed up a bit because it takes a few seconds to generate the full image. The reason I set the dpi so high is because of the way parallel curves work with line thickness. https://en.wikipedia.org/wiki/Parallel_curve

But I will say, the curves look really smooth.

## Example NFTs Don't Right-Click, Save As
<img src='bean_nft_0.png' width=40% height=40%> <img src='bean_nft_1.png' width=40% height=40%>
