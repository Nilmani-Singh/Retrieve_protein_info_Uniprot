import traceback, sys
import urllib
import urllib.parse
import urllib.request
import re
import xlsxwriter



def write_to_dict(dict1, code, name, domain, length, Isoforms, PDB,fname):
    
    try:
        if 'ID' in dict1.keys():
            dict1['ID'].append(code)
            dict1['Name'].append(name)
            dict1['Uniprot_Domains'].append(domain)
            dict1['Length'].append(length)
            dict1['Isoforms'].append(Isoforms)
            dict1['PDB_ID'].append(PDB)
            dict1['Full name'].append(fname)

        else:
            dict1['ID'] = [code]
            dict1['Name'] = [name]
            dict1['Uniprot_Domains'] = [domain]
            dict1['Length'] = [length]
            dict1['Isoforms'] = [Isoforms]
            dict1['PDB_ID'] = [PDB[2:-2]]
            dict1['Full name'] = [fname]
            
        return dict1  
    
    except:
        traceback.print_exc(file=sys.stderr)
    

        
        
def Retrieve_Uniprot_info(filename):
    try:
        f = open(filename, 'r')
        dict1 = dict()        
        counter = 0

        for line in f:
            code = str(line)
            code = code.strip()
            data = urllib.request.urlopen("http://www.uniprot.org/uniprot/" + code + ".txt").read()
            data = data.decode('utf-8')
            length = str(re.findall('Reviewed;\s+(.*)', data))
            PDB = str(re.findall('DR.*PDB;\s(.*);.*NMR', data))
            Isoforms  = str(re.findall('Named (isoforms=.*);',data))
            name = str(re.findall('ID\s+(.*)_.*Reviewed;', data))
            domain = str(re.findall('FT\s+DOMAIN.*\n.*note=(.*)', data))
            fname = str(re.findall('RecName:\s+Full=(.*)', data))
             
            dict1 = write_to_dict(dict1, code,name[2:-2],domain[2:-2],length[2:-3],Isoforms[2:-2],PDB[2:-2],fname[2:-3])
                   
            counter = counter + 1
            print(counter) # to display which entry# the script is working on 
        
        return dict1
    
    
    except:
        traceback.print_exc(file=sys.stderr)
        
        
def write_to_excel(filename):
    try:
        
        dict_val = Retrieve_Uniprot_info(filename) # call function
        print('Writing to excel...')
        excelname = filename[:-4] + '.xlsx' # make the filename end with .xlsx
        
        row = 0
        col = 0
        workbook = xlsxwriter.Workbook(excelname)
        worksheet = workbook.add_worksheet()
        
        for keys in dict_val.keys():
            row =  0
            col = col + 1
            worksheet.write(row, col, keys)
            for values in dict_val[keys]:
                row =  row + 1
                worksheet.write(row, col, values)
          
        
        workbook.close()
        
    except:
        traceback.print_exc(file=sys.stderr)
        
        
        
if __name__ == '__main__':
    
    filename = input('Enter filename (e.g. Example_Uniprot_ID_List.txt):   ')
    write_to_excel(filename)
    print('Finished!!')
