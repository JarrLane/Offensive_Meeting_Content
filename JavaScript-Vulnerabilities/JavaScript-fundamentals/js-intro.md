Here I will start learning basic Javascript, I will try to get the important concepts down and give some good examples. Im going to primarily use W3 schools and summarize what i learn from there in my own words.

Before you continue, I would say you are required to have at least some basic programming understanding because im going to write these notes in a way that someone without any programming knowledge will struggle to keep up with. I also 
reccomend you have a basic understanding of html and css, if not ill try to summarize as basic as possible when it comes up. Apart from that you should be fine.

JavaScript is primarily used to program the behavior of web pages. We can use it to change the HTML that is displayed to us. (If you dont know what HTML is, it is hypertext markup language, it is what we actually see when using a website)
Typically we can see the javascript inserted within the HTML when we inspect a pages source using f12, this is contained within ```<script> </script>```. We can also find JavaScript contained in external files that are referred to, these files
end in .js, and we can refer to them in the html using src like so: ```<script src="myScript.js"></script>``` Along with that, we can also reference external js code (im going to start saying js instead of JavaScript because its faster) 
by refering to a link that goes to js code or a file path to js code. 

To see the output/result of js code, we can use an html element, html output, alert boxes, or the browser console. (What is an HTML element? it is a part or section of the html that makes up a certain part of what we see, like a paragraph 
or maybe a header, it is made up of two tags, with the contwnt in the middle, so ```<p>This is paragraph content.</p>``` is an element and we use the tags p to know this is a paragraph, and the content inside is what makes up the paragraph,
we use multiple html elements to make up an html document, elements can also be "nested" or put inside each other) There is a method called innerHTMl that js will use to change the contents of an html element, and to access this element we
want to change we use document.getElementById(id), so here: 
```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = "<h2>js changed me from a blank element to this</h2>";
</script>
```
We reference the id of the paragraph element and change its contents, and we will see this change displayed to us. If we want to change just the text of an element we can use innerTEXT too. There is also document write, this will write to
html but it should be used with caution because if it is used after a page is loaded it gets rid of all the other html. Using window.alert or alert will show a popup of some output. console.log() can also display output in the console in the
browser, usually for debugging. I will get into more specifics of what things like window and console means soon but for now as long as you understand that these functions show js output you are good.

If you are familiar with basic programming you know that we use statements, which are instructions that are executed. Same with js. We can separate js statements with ;. Using multiple statements to define a procedure can be contained in 
brackets such as { }, which we can call code blocks, this is often how functions are made. Js also has its own keywords that indicate what the program will do, some basic keywords: use var to declare a variable, use let to declare a block 
variable, use const to declare a block constant, use if for conditional statements, use switch for switch statements, use for to make a block of statements that will execute in a loop, use function to declare a function, return to exit a
function, and use try to handle errors if a block of code doesnt work. I'll get into the difference between var and let soon.

In js there are two types of values, fixed (wont change) and variable (can change).


