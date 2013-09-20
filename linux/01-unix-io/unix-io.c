#include <stdio.h>

#define FOR_READ "/file-samples/for-read.txt"
#define FOR_EDIT "/file-samples/for-edit.txt"

static void read_file();
static void edit_file();
static void create_file();

int main(void) {


  // following functions implement the most basic file i/o functionalities

  read_file();
  edit_file();
  create_file();

  


  return 0;

}

/*===============================================================================
 * following functions implement the most fundamental file i/o functionalities
 *  1. read a file
 *  2. write an existing file
 *  3. creat a new file 
 *===============================================================================*/

static void
read_file() {


}

static void
edit_file() {


}

static void
create_file() {


}



/*===============================================================================
 * Following are  detailed examples of file related system-calls
 *  1. int      open()
 *  2. ssize_t  read()
 *  3. ssize_t  write()
 *  4. int      create()
 *  5. int      close()
 *  6. off_t    lseek()
 *===============================================================================*/
