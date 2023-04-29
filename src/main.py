import openai
from dotenv import dotenv_values


env = dotenv_values("./src/.env")
openai.api_key = env['OPENAI_API_KEY']

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
def gpt3_completion(
        prompt,
        engine='text-davinci-003',
        temp=0.7,
        top_p=1.0,
        tokens=400,
        freq_pen=0.0,
        pres_pen=0.0,
        stop=None
):
    if stop is None:
        stop = ['TIOTHERE:', 'YOU:']
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    # criar uma instância do Completion
    completion = openai.Completion()
    # criar a IA
    response = completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    return response['choices'][0]['text'].strip()


if __name__ == '__main__':
    conversation = []
    # executar
    while True:
        YOU_input = input('YOU: ')
        conversation.append(f'YOU: {YOU_input}')
        text_block = '\n'.join(conversation)
        prompt = open_file(
            './src/prompt_chat.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + '\TIOTHERE:'
        response = gpt3_completion(prompt)
        print('TIOTHERE:', response)
        conversation.append(f'TIOTHERE: {response}')
