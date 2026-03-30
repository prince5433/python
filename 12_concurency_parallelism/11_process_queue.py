from multiprocessing import Process, Queue
def prepare_chai(q):
    q.put("Masala chai is ready")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=prepare_chai, args=(q,))
    p.start()
    p.join()
    print(q.get())