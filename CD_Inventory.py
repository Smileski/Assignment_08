#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# LjSmileski, 2022-Dec-03, Edited file
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    #--- Fields ---#
    cd_id = 0
    cd_title = ' '
    cd_artist = ' '
    
    #--- Constructor ---#
    def __init__(self, cdid, cdtitle, cdartist):
        """Initializing private attributes.

        Private attributes:
            cd_id (int)
            cd_title (string)
            cd_artist (string)
        
        Returns:
            None.

        """
        #--- Attributes ---#
        self.__cd_id = cdid
        self.__cd_title = cdtitle
        self.__cd_artist = cdartist
        
    #--- Properties ---#
    """Creating properties (getter and setter) for each attribute.

    Private attributes:
        cd_id (int)
        cd_title (string)
        cd_artist (string)
    
    Returns:
        None.

    """
    # Creating properties (getter and setter) for each private attribute
    @property
    def idCD(self):
        return self.__cd_id
    
    @idCD.setter
    def idCD(self, value):
        if str(value).isnumeric():
            self.__cd_id = value 
        else:
            raise Exception('Enter integer for cd_id')
    @property
    def titleCD(self):
        return self.__cd_title
    
    @titleCD.setter
    def titleCD(self, value):
            self.__cd_title = value 
            
    @property
    def artistCD(self):
        return self.__cd_artist
    
    @artistCD.setter
    def artistCD(self, value):
            self.__cd_artist = value 

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from a list of lists to file

        Writes the data from 2D table (list of lists) into a file,
        one liust in table represents one line in the file

        Args:
            file_name (string): name of file used to write the data
            lst_Inventory (list): List od lists where we write data, we store the objects

        Returns:
            None.
        """
        # TOdone Add code here
        strRow = ''
        try:
            objFile = open(file_name, 'w')
            for row in lst_Inventory:
                for itemInRow in row:
                    strRow += str(itemInRow) + ', '
                strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
            objFile.close()
        except IOError:
            print('Unhadled error while reading the file!')
    
    @staticmethod
    def load_inventory(file_name, listTable):
        """Reads table data from file file_name
        
        Args:
            file_name (string): name of file used to write the data
            listTable (list): List of lists where we read data
             
        Returns:
            None
        """
        try:
            objFile = open(file_name, 'r')
            for row in objFile.readline():
                for itemInRow in row:
                    data = itemInRow[:-1].strip().split(',')
                listTable.append(data)
            objFile.close()
            
        except FileNotFoundError:
            print('File not found! Creating new file')
            objFile = open(file_name, 'w')
        except IOError:
            print('Unhadled error while reading the file!')
        return listTable    

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[i] Show Current Inventory\n[a] Add CD\n[s] Save Inventory to file')
        print('[l] Load Inventory from file\n[x] Exit\n')
        
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(listTable):
        """Displays current inventory table

        Args:
            table (list of lists): 2D data structure that holds the data during runtime.

        Returns:
            None.

        """
        print ('ID\t', 'CD Title\t', 'Artist Name\t')
        for row in listTable:
            for itemInRow in row:
                print(itemInRow , end = '\t\t')
            print()
        print('\n Displayed current Invetory! \n') 
    
    @staticmethod
    def add_cd():
        """Function asks user to input ID, CD title and artist name

        Args:
            None.

        Returns:
            user inputs newID, newTitle and newArtist.
         """     
        while True:
            try:
                newID = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print('You entered wrong value!Please enter number for ID!')
        newTitle = input('What is the CD\'s title? ').strip()
        newArtist = input('What is the Artist\'s name? ').strip()  
        return newID, newTitle, newArtist   

# 1. When program starts, load data file from inventory
    try:
        listTable = FileIO.load_inventory(strFileName, lstOfCDObjects)
    except FileNotFoundError:
        print('File does not exist.')
        FileIO.save_inventory(strFileName, lstOfCDObjects)

# -- Main Body of Script -- #

# 2. Start main loop
while True:
    # 3. Display menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # 4. Menu selection
    
    # 4.1 Exit
    if strChoice == 'x':
        print('Goodbye!')
        break
    
    # 4.2 Load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            listTable = FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(listTable)
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        continue 
        
    # 4.3 Add a CD
    elif strChoice == 'a':
        cd_id, cd_title, cd_artist = IO.add_cd()
        lstTbl = [cd_id, cd_title, cd_artist]
        lstOfCDObjects.append(lstTbl) 
        IO.show_inventory(lstOfCDObjects)
        continue 
        
    # 4.4 Display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue
    
    # 4.5 Save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  
    # 4.6 Catch all general errors!
    else:
        print('General Error')



