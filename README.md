<h1 align='center'>The Bread App!</h1>

<h1 align='center'><img src="https://images.unsplash.com/photo-1597604396383-b8ca64ed8fa7?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=967&q=80" alt="" srcset="" width="400"></h1>

<h3>This python progam will convert a recipe that uses commercial yeast into a sourdough recipe.  For now is striaght CLI, but there are plans for a GUI in the future.</h3>

<h3><a href="https://repl.it/@ljensen505/ImpracticalMediocreSeahorse#main.py" target="_blank">Repl.it Preview</a></h3>

<h4>Known Issues:</h4>
    <ul>
        <li>it's ugly</li>
        <li>BUG: improper handling of decimal in original recipe. 10.5g of salt -> 210g, but 10g is handled properly</li>
        <li>If a liquid is used in place of water (such as milk), there will be unexpected results.  Using milk isn't recommended anyway though because of how long this dough takes to rise.</li>
        <li>tell user to not input baker's yeast whatoever</li>
    </ul>

<h4>Requirements:</h4>
    <ul>
        <li>Python3</li>
    </ul>

<h4>Notes</h4>
    <ul>
        <li>Everything is in grams. Including "g" in your input is optional. 1000g == 1000</li>
        <li>You need experience making sourdough. Timings will be off, but dough volume increases should be the same.  This program won't give you detailed instructions - it only converts your ingredient list.</li>
    </ul>