// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    //should be case insensitive

    //hash the word with hash function

    //access the linked list at that index in the hash table

    //go through linked list, looking for the word with strcasecmp
    //check youtube for visual!!
    //start with checking word against first item of linked list
    //keep going through list until you get NULL
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';


}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    //open dictionary file - use fopen - check if return == NULL

    //read strings from dictionary file
    //fscanf(file, "%s", word) ------- FILE = pointer u get from fopen
    //run fscanf on each word of the dictionary
    //until fscanf returns EOF (loop fscanf until EOF)

    //Create a new node for each word
    //use malloc -- check if return == NULL -- strcpy word into node

    //use a hash function that
    //takes a string and returns an index

    //insert the node into hash table
    //hash tables are a an array of linked lists!!
    //look at youtube for visual
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    //youtube for visual
    return false;
}
