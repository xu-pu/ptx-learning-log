#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

/***********************************************************************
 *
 * This snippet of C code demonstrates how POSIX semaphore and pthread 
 * solves the producer-consumer problem
 *
 ***********************************************************************
 * pthread APIs
 ***********************************************************************
 *
 * pthread_create -- create new thread
 * pthread_join -- wait for the termination of specific thread 
 * pthread_exit -- terminate current thread
 * pthread_cancel -- terminate specific thread
 *
 ***********************************************************************
 * pthread-mutex APIs
 ***********************************************************************
 *
 * pthread_mutex_init
 * pthread_mutex_destroy
 * pthread_mutex_lock
 * pthread_mutex_trylock
 * pthread_mutex_unlock
 *
 ***********************************************************************
 * semaphore APIs
 ***********************************************************************
 *
 * semaphore is a multi-thread/process compatiable counter (>=0)
 * sem_init
 * sem_post -- semaphore++
 * sem_wait -- semaphore > 0 ? semaphore-- : wait-try-again
 * sem_trywait -- semaphore > 0 ? semaphore-- : move-on
 *
 ***********************************************************************/

#define BUFFER_SIZE 10
#define SUM_SIZE 100

int buffer[BUFFER_SIZE];
int b_stack_pointer = 0;

static void put_item(int);
static void get_item(int *);

static void * producer (void *);
static void * consumer (void *);

sem_t sem_items;
sem_t sem_slots;

int sum = 0;
int producer_done = 0;

pthread_mutex_t buffer_lock        = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t producer_done_lock = PTHREAD_MUTEX_INITIALIZER;

/***********************************************************************
 * Parent Process
 ***********************************************************************/

int main (void) {

  pthread_t prod_id;
  pthread_t cons_id;

  sem_init(&items, 0, 0);
  sem_init(&slots, 0, BUFFSIZE);
  
  pthread_create(&prod_id, NULL, producer, NULL);
  pthread_create(&cons_id, NULL, consumer, NULL);

  pthread_join(prod_id, NULL);
  pthread_join(cons_id, NULL);

  printf("sum = %d\n", sum);

}

/***********************************************************************
 * Producer Thread
 ***********************************************************************/

static void * producer (void * arg1) {
  for (int i = 1 ; i < SUMSIZE ; i++) {
    sem_wait(&sem_slots);
    put_item(i);
    if (i == SUMSIZE) {
      // acccess shared area [producer_done]
      pthread_mutex_lock(&producer_done_lock);
      producer_done = 1;
      pthread_mutex_unlock(&producer_done_lock);
      // lock-operate-unlock
    }
    sem_post(&sem_items);
  }
    return NULL;
}

/***********************************************************************
 * Consumer Thread
 ***********************************************************************/

static void * consumer (void * arg2) {
  int myitem;
  while (true) {
    pthread_mutex_lock(&producer_done_lock);
    if (producer_done == 1) {
      pthread_mutex_unlock(&producer_done_lock);
      if (sem_trywait(&items)) break; // no item left
    } 
    else {
      pthread_mutex_unlock(&producer_done_lock);
      sem_wait(&items);
    }

    // acccess shared area [buffer] 
    pthead_mutex_lock(&buffer_lock);
    get_item(&myitem);
    pthread_mutex_unlock(&buffer_lock);
    // lock-operate-unlock

    sem_post(&slots);
    sum += myitem; 

  }
  return NULL;
}

/***********************************************************************
 * Buffer put and get
 ***********************************************************************/

static void put_item (int value) {
  b_stack_pointer++;
  buffer[b_stack_pointer] = value;
}

static void get_item (int * addr) {
  *addr = buffer[b_stack_pointer];
  b_stack_pointer--;
}
