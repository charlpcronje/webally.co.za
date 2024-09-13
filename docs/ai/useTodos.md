<prompt>
    <overview>
        - In a previous context window, I asked you to give me all the files for this website, but only to give me the TODO's in each file. Then I created all of those files with the TODO's saved inside each file, I then combined all the files in `todos.md`.
        - Look at every file and every TODO and sub-todo's that you will find in each file
        - Be meticulous and for every class, method or function make sure you are evaluating all the other TODO's so that the code can be reused and imported where needed and not recreated, th TODO's are very granular so it should give you a very good guideline to what exactly needs to be in every file
    </overview>
    
    <instructions>
        <file>
            Have a look at `todos.md`. It contains all the files that I created, combined as Markdown with a code block for each file. You can then see exactly what files there are, how they should reference each other, how they should import each other to create the full website without losing context.
        </file>
        
        <techStack>
            Have a look at `techStack` added to the project. It specifies the tech stack and what you can expect to already be installed.
        </techStack>
        
        <scripting>
            I'm not sure if it is the best to use typescript for everything in this SvelteKit project as the ui components are all made in TypeScript, but I don't think it's necessary if it's only going to take more time and if it's going to cause more errors, rather use Javascript with jsDoc. But it is TS is needed then use it. But whatever it is, choose the option that will make the development time the least
        </scripting>

         <shadcn>
            The following components are available from ShadCN
            I added a document called shadcn.md where you can find all the components, if they are already installed or not and how to use them and how to use them.

        </shadcn>
    </instructions>
    
    <request>
        <detail>Please let me know if there's anything that you need. Please start the first file, and then the next and the next.</detail>
        <rules>
            <rule>* Please create production-ready code only.</rule>
            <rule>* Please do not omit any code.</rule>
            <rule>* Please do not add any placeholders instead of the code.</rule>
            <rule>* Please add comments to all of the code with the argument types and return types.</rule>
            <rule>* Please do error handling for everything.</rule>
            <rule>* Please add the file name to the first line of each file and comments.</rule>
        </rules>
    </request>
    
    <important>
        <detail>If there are any parts of the system you are not sure of, or you are not sure about the best implementation, then please reason about the implementation.</detail>
        <reasoning>
            To reason about something, follow these steps
            1. Come up with 3 solutions to the problem. Rate each solution out of 10, with 3 criteria of your choosing, and give it an average score allowing for 2 decimals. 
            2. If you feel that there's still a better solutions available, then create another 3, and also rate them the same way. Repeat step 2 until you have 2 solutions that you are happy with.
            3. Choose the best solution from each set of solutions and iterate on them. Create the final code for the solution with the highest rating.
        </reasoning>
        <final>
            
        </final>
    </important>
</prompt>
