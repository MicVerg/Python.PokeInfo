# PokeInfo
#### Video Demo:  <https://youtu.be/iqGzKAzy9_k>
#### Description: A lightweight PokeDex that shows only the information I used to want to see as a kid growing up ..
Powered by https://pokeapi.co/docs/v2.
I really wanted to learn how API's work and didn't know anything about them before this little project.
Initially I had other ideas for projects, but I had issues finding access to the API's I needed for those ideas, so the pokeapi was a blessing!

The app is very lightweight using only Python - Flask and making calls to different pokeapi pages, combining those calls to navigate through the pokedex.
I didn't pay a lot of attention to design, I really just wanted to focus on how I could get data out of the API and how I could display it properly.

There's only 4 HTML pages, index, layout, pokedex and result and 1 python file, app.py.

App.py
I started this by extracting some of the easier data out of the pokeapi, like height and weight, to get to know how it actually works.

Then flavor texts, which needed quite some clean-up, they needed to be divided into certain versions of the games to actually work.
These texts also needed clean-up because it contained \u000c, &shy and \xad characters which all gave display issues (wrong spacing etc).

Next up was probably the hardest part for me personally, evolution-to.
Evolutions in the pokeapi are in a different table, so you have to compare the 2, but the hardest about this was understanding how I could make conditionals and use the nested entries to get either evolution #1 or #2, depending on what pokemon is selected at the moment.
It took me a while to understand..

More evolutions later, with wanting to display evolution-from, which was a lot easier than evolution-to, knowing what I had learned, also the entry was more comfortable to reach and there aren't any nested entries for this.

It also took me a while to understand that I can (and should?) just copy the code from POST to GET, with some slight adjustments.



HTML
The HTMLs speak for itself I suppose, I did not spend a lot of time on design here because I don't really enjoy that.
The most interesting in the HTMLs was manipulating the Jinja conditionals into the thing I needed, or if the "no evolution" image had to be shown etc.
Also added a small eventlistener so you can use the arrow-keys to stroll through the pokedex.