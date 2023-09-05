from pyparsing import QuotedString

def format_chat_template(input_text):
    gen_command = "{{gen" + QuotedString("'") + "}}"
    if gen_command.searchString(input_text):
        user_content = input_text.split(gen_command.searchString(input_text)[0][0])[0].strip()
        gen_command_content = gen_command.searchString(input_text)[0][1]
        user_segment = "{{#user}}" + user_content + "{{/user}}"
        assistant_segment = "{{#assistant}}" +"{{gen '"+ gen_command_content+"'}}" + "{{/assistant}}"
    else:
        # When gen_command is not present, enclose the entire input_text in user tags
        user_segment = "{{#user}}" + input_text + "{{/user}}"
        assistant_segment = "{{#assistant}}{{gen 'write'}}{{/assistant}}"
    return user_segment + " " + assistant_segment
input_text = "Tweak this proverb to apply to model instructions instead. Where there is no guidance{{gen 'rewrite'}} "
formatted_text = format_chat_template(input_text)
print(formatted_text)

