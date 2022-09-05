#! /usr/bin/env python
import yaml
import argparse

def formatter(input, ftype):
    if (ftype == 'scored'):
        if (input):
            return("Scored")
        else:
            return "Not Scored"
    elif(ftype == 'enabled'):
        if (input):
            return "x"
        else:
            return ""
    elif(ftype == 'notenabled'):
        if (input):
            return ""
        else:
            return "x"
    elif(ftype == 'notsupported'):
        if (input):
            return "x"
        else:
            return ""
    else:
        return("ERROR")

def read_gfile(filetoread):
    with open(filetoread,'r') as stream:
        try:
            return(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)

def generate_csv(ifile,ofile):
    rules_list=read_gfile(ifile)
    outfile = open( ofile, 'w+' )
    headers='RuleID;Rule Description;Scored;Severity;Applied rules;Disabled Rules;NotSupported;Observations\n'
    outfile.write(headers)
    for entry in rules_list["rules"]:
        if(not rules_list["rules"][entry]['enabled']):
            try:
                #append=entry + ';' + rules_list["rules"][entry]['description'] + ';' + str(rules_list["rules"][entry]['scored']) + ';' + rules_list["rules"][entry]['severity'] + ';' + str(rules_list["rules"][entry]['enabled']) + ';' + str(rules_list["rules"][entry]['not_supported']) + ';' + rules_list["rules"][entry]['observations'] + '\n'
                append=entry + ';' + rules_list["rules"][entry]['description'] + ';' + formatter(rules_list["rules"][entry]['scored'],'scored') + ';' + rules_list["rules"][entry]['severity'] + ';' + formatter(rules_list["rules"][entry]['enabled'],'enabled') + ';' + formatter(rules_list["rules"][entry]['enabled'],'notenabled') + ';' + formatter(rules_list["rules"][entry]['not_supported'],'notsupported') + ';' + rules_list["rules"][entry]['observations'] + '\n'
            except:
                #append=entry + ';' + rules_list["rules"][entry]['description'] + ';' + str(rules_list["rules"][entry]['scored']) + ';' + rules_list["rules"][entry]['severity'] + ';' + str(rules_list["rules"][entry]['enabled']) + ';False;' + rules_list["rules"][entry]['observations'] + '\n'
                append=entry + ';' + rules_list["rules"][entry]['description'] + ';' + formatter(rules_list["rules"][entry]['scored'],'scored') + ';' + rules_list["rules"][entry]['severity'] + ';' + formatter(rules_list["rules"][entry]['enabled'],'enabled') + ';' + formatter(rules_list["rules"][entry]['enabled'],'notenabled') + ';;' + rules_list["rules"][entry]['observations'] + '\n'
        else:
            #append=entry + ';' + rules_list["rules"][entry]['description'] + ';' + str(rules_list["rules"][entry]['scored']) + ';' + rules_list["rules"][entry]['severity'] + ';' + str(rules_list["rules"][entry]['enabled']) + ';False;\n'
            append=entry + ';' + rules_list["rules"][entry]['description'] + ';' + formatter(rules_list["rules"][entry]['scored'],'scored') + ';' + rules_list["rules"][entry]['severity'] + ';' + formatter(rules_list["rules"][entry]['enabled'],'enabled') + formatter(rules_list["rules"][entry]['enabled'],'notenabled') + ';;;\n'
        outfile.write(append)
    outfile.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='generate csv file from dictionary')

    parser.add_argument('--input','-i',
                    help='path to the file containing the "rules" dictionary (example: defaults/main.yml)')
    parser.add_argument('--output','-o',
                    help='path to the destination csv file')

    args = parser.parse_args()
    try:
        input_file=args.input
        output_file=args.output
        print(input_file + ' -> ' + output_file)
        generate_csv(input_file,output_file)
    except:
        parser.print_help()
