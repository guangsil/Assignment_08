#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Guang-Sin Lu, 2022-Mar- 19, cleaning up code, write class cinstructors, attribute
# Guang-Sin Lu, 2022-Mar- 19, write code of main loop
# Guang-Sin Lu, 2022-Mar- 20, Testing, cleaning and documenting
#------------------------------------------#

#Define class/constructor/Property
class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # Add Code to the CD class
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except ValueError:
            raise ValueError("CD ID must be an integer")

    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        self.__title = str(value)

    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = str(value)

    # -- Method -- #
    def __str__(self):
        return int(self.__cd_id)+'/'+str(self.__cd_title) +'/'+str(self.__artist)
    
    
    
# -- PROCESSING -- #

class DataProcessor():
    #  Add functions for processing CD data
   """Processing the data from user selection, add delete or save"""
   
   
   @staticmethod 
   def add_inventory(lst_Inventory,cd_id, cd_artist, cd_title):
       """
       Function to add new data to list.
       
       Args:
           cd_id (int): ID representing the ID of the new CD
           cd_title (string): Title of the new CD
           cd_artist (string): Artist of the new CD
           lst_inventory(list of list): 2D data structure (list of dicts) that holds the data during runtime
            
       Returns:
           lst_inventory (list of list): 2D data structure (list of dicts) that holds the data during runtime
            
       """
       new_cd = CD(cd_id, cd_title, cd_artist)
       lst_Inventory.append(new_cd)
       return lst_Inventory

   @staticmethod
   def delete_inventory(lst_Inventory):
        """
        Function to delete CD from user input.
        
        Args:
            table (list of dict): 2D data structure (list of dicts) 
            that holds the data during runtime
            
        Returns:
            Removes data associated to ID user input held in the table
        """
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        while True:
            try:
                int(intIDDel)
                break
            except ValueError:
                intIDDel = input('Error: ID must be an integer. Enter ID: ').strip()
        # 3.5.2 search thru lstTbl and delete CD
        intRowNr = -1
        blnCDRemoved = False
        for row in lst_Inventory:
            intRowNr += 1
            if row.cd_id == intIDDel:
                del lst_Inventory[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return lst_Inventory

class FileIO:
    """
    Processes data to and from file:

    properties:
        None

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # Add code to process data from a file
    
    @staticmethod
    def load_inventory(file_name, lst_Inventory):   
        """
        Function to read the data from file identified by file_name

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure that holds the data during runtime

        Returns:
            lst_Inventory (list of dict): a list of CD objects
            
            
            new_cd = CD(cd_id, cd_title, cd_artist)
            lst_Inventory.append(new_cd)
            return lst_Inventory
        """
       
        try:
            lst_Inventory.clear()  # this clears existing data and allows to load data from file
            with open(file_name, 'r') as objFile: 
                for row in objFile:
                    lstRow = row.strip().split(",")
                    cd_attributes = CD(lstRow[0], lstRow[1], lstRow[2])
                    lst_Inventory.append(cd_attributes)
            objFile.close()
        except FileNotFoundError as err:
            print(err, "The file {} could not be loaded".format(file_name))
        finally:
            return lst_Inventory
    
    # Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        
        """
        Function to save data to file from list
        
        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        
        Returns:
            None.
        """
        with open(file_name, 'w') as objFile:
            for row in lst_Inventory:
                newcd=(str(row.cd_id),row.cd_artist,row.cd_title)
                objFile.write(','.join(newcd) + '\n')
            objFile.close()
              

# -- PRESENTATION (Input/Output) -- #
class IO:
    #add docstring
    """Handling Input / Output"""
    
    # add code to show menu to user
    @staticmethod
    def print_menu():
        """
        Displays a menu of choices to the user
        
        Args:
            None.
            
        Returns:
            None.
        """

    print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
    
    # add code to captures user's choice
    def menu_choice():
        """
        Gets user input for menu selection
        
        Args:
            None.
            
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        
        choice = ' '
        try:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
            while choice not in ['l', 'a', 'i', 'd', 's', 'x']: 
                raise ValueError('That is not a valid choice!') 
        except ValueError as e:
            print(type(e))
            print('Please enter one of the offered options from menu') 
        else:   
            print("Thank you for entering a valid choise, please continue:")
            return choice
    
    # add code to display the current data on screen
    @staticmethod
    def show_inventory(lst_Inventory):
        """
        Displays current inventory table
        
        Args:
            table (list of dict): 2D data structure that holds the data during runtime.
        
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
        print('======================================')
        
    #add code to get CD data from user
    @staticmethod
    def get_UserInput():
       """
       Function to add User input
       Gets input from user for ID, Title and Artist to be save in table
       
       Args:
           None.
       
        Returns:
           ID (interger): ID representing the ID of the new CD
           Title (string): Title of the new CD
           Artist (string): Artist of the new CD
       """
       ValidID =False
       while not ValidID:
           try:
               ID = int(input('Enter ID: ').strip())
               if ID <=0:
                   raise ValueError('That is not a positive integer number!') 
           except ValueError:
               print('Please enter ID using positive integers')
           else:
               ValidID=True
       Title = input('What is the CD\'s title? ').strip()
       Artist = input('What is the Artist\'s name? ').strip()
       return ID, Title, Artist


# -- Main Body of Script -- #
# Add Code to the main body
def main(): 
    # -- DATA -- #
    strFileName = 'CDInventory.txt'
    lstOfCDObjects = []
    strChoice = '' # User input

# Load data from file into a list of CD objects on script start
# 1. When program starts, read in the currently saved Inventory
    lstOfCDObjects = FileIO.load_inventory(strFileName,lstOfCDObjects)
    
# Display menu to user
    # show user current inventory
# 2. start main loop
    while True:
        # 2.1 Display Menu to user and get choice
        IO.print_menu()
        strChoice = IO.menu_choice()
# 3. Process menu selection
        
    # let user add data to the inventory
# 3.3 process add a CD
        if strChoice == 'a':
# 3.3.1 Ask user for new ID, CD Title and Artist
            strID, strTitle, strArtist = IO.get_UserInput()
# 3.3.2 Add item to the table
            DataProcessor.add_inventory(lstOfCDObjects, strID, strTitle, strArtist)
            IO.show_inventory(lstOfCDObjects)
            continue 
    # start loop back at top.
    # let user save inventory to 
        elif strChoice == 's':
# 3.6 process save inventory to file
# 3.6.1 Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstOfCDObjects)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
# 3.6.2 Process choice
            if strYesNo == 'y':
            # 3.6.2.1 save data
                FileIO.save_inventory(strFileName, lstOfCDObjects)
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue  # start loop back at top.

# 3.2 process load inventory
    # let user load inventory from file
        elif strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'Y\' to continue and reload from file. otherwise reload will be canceled. ')
            if strYesNo.lower() == 'y':
                print('reloading...')
                lstOfCDObjects = FileIO.load_inventory(strFileName,lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            continue  # start loop back at top.

# 3.4 process display current inventory
     # process display current inventory
        elif strChoice == 'i':
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
            
# 3.5 process delete a CD
        elif strChoice == 'd':
# 3.5.1 get Userinput for which CD to delete
            IO.show_inventory(lstOfCDObjects)
            lstOfCDObjects = DataProcessor.delete_inventory(lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
            
    # let user exit program
# 3.1 process exit 
        elif strChoice == 'x':
            break

# 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
        else:
            print('General Error')

main()
("\n\nPress the enter key to exit.")   
