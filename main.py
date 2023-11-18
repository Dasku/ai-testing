import openai
import os

from openai import OpenAI
from dotenv import load_dotenv


# secrets for API keys
env_path = os.path.join(os.path.dirname(__file__), '..', 'secrets', '.env')
load_dotenv(env_path)

openai.api_key = os.getenv("OPENAI_API_KEY")

article="LONDON, July 1, 1908 (UP) -- One thousand suffragettes, goaded into madness by the action of the police, to-day attempted to rescue twenty-eight of the twenty-nine of their number who were arrested during last night's unprecedented demonstration in Parliament square. These twenty-eight were in a prison van and were being hauled to prison, when a mob of enraged women 'rushed' the van, just as it was leaving the courtyard. Expecting the attack, hundreds of police were hidden inside the courtyard and, at the first movement by the suffragettes, they rushed out and beat back the women. The van drove off at a mad gallop, the prisoners being assailed with cheers and shrieking good-byes from the baffled host behind The court gave the prisoners the option of being placed under peace bonds, running from $20 to $250, or going to prison for from one to three months. But one woman agreed to give bond, the others preferring the martyr role. Before the trial of the women, Mrs. Parkhurst, one of the leaders, held a conference with her lieutenants and it was decided to raid the police court, in an effort to prevent the trials. They had charges drafted against the police, supported by scores of affidavits, showing that the police acted with unwarranted brutality in arresting the women and that scores had been injured by the police. The suffragettes have decided to re peat last night's performance every night, until Parliament finally grants them the right of franchise. Fearing to-day's demonstration, 5,000 extra police were in readiness for any emergency. The streets leading to the police station were massed with suffragettes and spectators drawn to the scene by the promise of trouble. At almost every corner, women speakers harangued the crowds and assailed Premier Asquith for his refusal to receive the deputation that called on him yesterday. The courtroom where the women were tried was packed to suffocation by suffragettes and sympathizers and the threat was openly made that, if the women were sentenced to prison for their conduct of last night, the jails of London could not hold the number that the police would be called upon to arrest to-night in a proposed demonstration of protest. Most of the women in jail had their handbags with them, as they expected to be sent to prison for a term of considerable length. Many society women were present at the court hearing, one of them being the wife of Earl Russell, who deeply sympathizes with the suffragettes. The women say that the action of the police in arresting their sisters last right was an unwarranted outrage. Mrs. Pankhurst, one of those who sought an audience with the premier, was particularly bitter in her condemnation of the police. The spectacle of last night set a new mark for Londoners. For nearly four hours, a vast army besieged the House of Commons and clamored to be received by the premier. While the demonstration was at its height, Premier Asquith slipped quietly from a side door and made his escape. A small fleet of police boats patrolled the Thames river to prevent assaults by water. The crowd was remarkably well behaved, though the police persisted in dragging away the women who raised their voices too loud in demanding the right to vote. All through the demonstration, important debates were taking place. Many members, however, left the chamber to watch the demonstration from the palace yard."

# Definition of our local function(s).
# This is effectively telling ChatGPT what we're going to use its JSON output for.
functions = [
    {
        "name": "write_post",
        "description": "Shows the title and summary of some text.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title of the text output."
                },
                "summary": {
                    "type": "string",
                    "description": "Summary of the text output."
                }
            }
        }
    }
]

# The request to the ChatGPT API.

response = openai.ChatCompletion.create(
    model = "gpt-3.5",
    messages = [
        {
            "role": "system",
            "content": "You are a useful assistant."
        },
        {
            "role": "user",
            "content": f"Here is an article: {article}. Please return a title and summary."
        }
    ],
    functions = functions,
    function_call = {
        "name": functions[0]["name"]
    }
)

print(response)
