// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "dictionary.h"
#include <stdlib.h>

#include "speller.c"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
unsigned int counter = 0;

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
    return tolower(word[0]) - 'a';

//sources:
//https://stackoverflow.com/questions/31930046/what-is-a-hash-table-and-how-do-you-make-it-in-c
//https://stackoverflow.com/questions/64087044/do-you-have-any-simple-hash-function-that-takes-first-three-letter
//i will continue on the rest of the assignment first before improving this function
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open dictionary file - use fopen - check if return == NULL
    FILE *inputDict = fopen(dictionary, "r");
    if (inputDict == NULL)
        {
            printf("Could not open file.\n");
            return 1;
        }

    //read strings from dictionary file
    //fscanf(file, "%s", word) ------- FILE = pointer u get from fopen
    //run fscanf on each word of the dictionary
    //until fscanf returns EOF (loop fscanf until EOF)
    char buffer[LENGTH + 1];
    while (fscanf(inputDict, "%s", buffer) != EOF)
    {
    //Create a new node for each word
    //use malloc -- check if return == NULL -- strcpy word into node
        node *a = malloc(sizeof(node));
        if (a == NULL)
        {
            return 1;
        }
    strcpy(a->word, buffer);
    //use a hash function that
    //takes a string and returns an index
    int hashResult = hash(buffer);

    //insert the node into hash table
    //hash tables are a an array of linked lists!!
    //look at youtube for visual
    a->next = table[hashResult];
    table[hashResult] = a;
    
    //counter for size
    counter++;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    //youtube for visual
    return false;
}
