# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran the game, the interface loaded and looked fine, but after playing it, I started noticing that some of the game behavior did not match what I expected. The app seemed functional on the surface, but the logic behind the guesses, game reset, and state handling had problems.

- List at least two concrete bugs you noticed at the start  
Bug 1: I expected the hint to tell me to go lower when my guess was greater than the secret number, but it told me to go higher instead. For example, when the debug panel showed the secret number was 65 and I guessed 88, the game responded with “Go HIGHER!” even though 88 was already above 65.

Bug 2: I expected clicking New Game to fully reset the game so I could start over normally, but it did not reset everything correctly. After I won my first game and tried to start a new one, the game still behaved as if the old game state was affecting the new round.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

For this project, I used AI as a support tool rather than as something to blindly follow. I used ChatGPT and Copilot to help me reason through the bugs, understand what the code was doing, and figure out what kind of fixes and tests made sense. If I were doing this inside VS Code, Copilot would also be useful for explaining specific functions and suggesting refactors, but I still needed to verify every suggestion myself.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example of a correct AI suggestion was identifying that the hint logic in check_guess() was reversed. The AI helped point out that when guess > secret, the code was returning “Too High” but the message incorrectly said “Go HIGHER!” instead of telling the player to go lower. I verified this by comparing the debug secret value to my guess and then seeing that the message on the screen did not match the actual relationship between the two numbers.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One example of an incorrect or misleading AI-related assumption was that the game looked fine at first glance, so it might seem like the state logic was correct. But after testing more carefully, I saw that the New Game logic did not fully reset the session state properly, especially the status and difficulty-related behavior. This reminded me that AI-generated or AI-reviewed code can look clean and still hide logic bugs that only show up during real use.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided whether a bug was really fixed by checking both the code and the actual game behavior. It was not enough for the code to “look correct” — I needed to run the Streamlit app again, play the game, and confirm that the result matched what I expected. I also looked at the debug info in the sidebar to compare the secret number, attempts, and score against the outputs the app was giving me.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One manual test I ran was guessing a number larger than the secret number shown in the debug panel. If the secret was 65 and I guessed 88, the correct behavior should be that the game tells me the guess was too high and suggests going lower. That test showed me the hint logic was broken in the original version, and after the fix, it would help confirm that the hint now matched the actual comparison.

- Did AI help you design or understand any tests? How?

I also used automated testing ideas through pytest for the guessing logic. For example, a test like check_guess(60, 50) should identify the guess as too high, while check_guess(40, 50) should identify it as too low. AI helped by suggesting the structure of these tests, but I still had to notice that my function returned a tuple, not just a single string, so I needed to verify the exact expected output carefully.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

In the original app, the secret number did not stay stable because Streamlit reruns the script whenever the user interacts with the app. If the app logic is not careful about how it stores values in st.session_state, variables can get recreated or reset in ways that feel random to the user. That means the secret number, attempts, or status can behave inconsistently if they are not properly initialized and reset.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain Streamlit reruns to a friend by saying that every button click or input change causes the script to run again from top to bottom. Session state is what allows the app to “remember” values like the secret number, score, and attempts between those reruns. Without session state, the app would behave like it was starting over every single time the user touched something.

- What change did you make that finally gave the game a stable secret number?

The change that finally gives the game a stable secret number is making sure the secret is only set when it is not already in st.session_state, and making sure a new value is assigned only during a true reset like clicking New Game. That way, the secret number stays the same throughout one round of the game and only changes when a fresh game actually begins.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

One habit from this project that I want to reuse is testing bugs with very specific examples instead of assuming I understand the problem from reading the code. In this project, checking the debug secret value and then making a deliberate guess above or below it helped me quickly confirm whether the hint logic was actually correct. That kind of targeted testing is something I want to keep using in future labs and projects.

  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?


  Next time I work with AI on a coding task, I would be even more careful about verifying the exact return values and behavior of functions before accepting a suggestion. For example, a test might look right at first, but if the function returns a tuple instead of a string, the test still needs to be written differently. That reminded me that AI can help generate code faster, but accuracy still depends on my understanding.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project changed the way I think about AI-generated code because it showed me that code can look polished and still contain major logic flaws. AI is useful for brainstorming, explaining, and speeding up parts of the process, but I still have to be the one who tests, verifies, and decides what is actually correct.