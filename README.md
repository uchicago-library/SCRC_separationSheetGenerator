Makes separation sheets

Run the script, open rendered.html in firefox.

Be sure in about:config you've changed the values of...

print.print_header{left,center,right} and print.print_footer{left, cneter, right}
to the emptry string, to avoid superfluous information getting printed on the sheets.

Flip the page layout to landscape and print away.

To test that everything is set up right you can also print to PDF, check things out,
and print the PDF once everything is good to go.

Also keep in mind that while current identifiers only need to be unique within their "batch"
it is _probably_ safer to keep them universally unique. This requires preserving the used_ids.json
file at the moment, until we can institute a more distributable solution.

This identifier scheme gives us 2176782336 possible IDs, but the implementation will start to probabalistically
fail far before we reach that number. This is a "feature" which stops the script from blocking infinitely, and also
a reminder to as to the potential weaknesses of this identifier scheme.
