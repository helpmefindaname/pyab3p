#include "FBase.h"

#ifdef __USE_FILE_OFFSET64
#define DWORD_HI(x) (x >> 32)
#define DWORD_LO(x) ((x)&0xffffffff)
#else
#define DWORD_HI(x) (0)
#define DWORD_LO(x) (x)
#endif

using namespace std;
namespace iret {

FBase::FBase(const char *typ, const char *nam) {
  size_t lxn = strlen(typ);
  type = new char[lxn + 1];
  strcpy(type, typ);
  lxn = strlen(nam);
  name = new char[lxn + 1];
  strcpy(name, nam);
  cflag = 0;
  oflag = 0;
  pflag = get_qflag();
  eflag = 1;
}

FBase::FBase(const char *typ, const char *nam, const char *pt) {
  size_t lxn = strlen(typ);
  type = new char[lxn + 1];
  strcpy(type, typ);
  lxn = strlen(nam);
  name = new char[lxn + 1];
  strcpy(name, nam);
  cflag = 0;
  oflag = 0;
  pflag = get_qflag();
  if (*pt != ':')
    set_path_name(pt);
  else
    set_path_internal(pt + 1);
}

FBase::~FBase(void) {
  delete[] type;
  delete[] name;
}

void FBase::change_type(const char *typ) {
  if (type != NULL)
    delete[] type;
  size_t lxn = strlen(typ);
  type = new char[lxn + 1];
  strcpy(type, typ);
}

void FBase::change_name(const char *nam) {
  if (name != NULL)
    delete[] name;
  size_t lxn = strlen(nam);
  name = new char[lxn + 1];
  strcpy(name, nam);
}

void FBase::subname(const char *tph, const char *tpl, const char *nm) {
  char cnam[max_str];
  size_t i = strlen(tpl);
  strcpy(cnam, tpl);
  cnam[i] = '_';
  cnam[i + 1] = '\0';
  strcat(cnam, nm);
  change_type(tph);
  change_name(cnam);
}

void FBase::set_path_internal(const char *pt) {
  size_t len;
  if (pt && (len = strlen(pt))) {
    eflag = 0;
    path = new char[len + 1];
    strcpy(path, pt);
  } else
    eflag = 1;
}

void FBase::set_path_name(const char *pa) {
  size_t len;
  if (pa && (len = strlen(pa))) {
    eflag = 2;
    pnam = new char[len + 1];
    strcpy(pnam, pa);
  } else
    eflag = 1;
}

void FBase::map_down(FBase *pFb) {
  pFb->change_type(type);
  pFb->change_name(name);
  pFb->pflag = pflag;
  if (eflag == 2)
    pFb->set_path_name(pnam);
  else if (!eflag)
    pFb->set_path_internal(path);
}

void FBase::map_down_sub(FBase *pFb, const char *subtype) {
  pFb->subname(type, name, subtype);
  pFb->pflag = pflag;
  if (eflag == 2)
    pFb->set_path_name(pnam);
  else if (!eflag)
    pFb->set_path_internal(path);
}

void FBase::get_pathx(char *nam, const char *ch) {
  char cnam[256];
  ifstream fin;

  if (eflag == 2) {
    strcpy(cnam, "path_");
    strcat(cnam, pnam);
    fin.open(cnam, ios::in);
    if (!fin.is_open()) {
      fin.clear();
      strcpy(cnam, "path");
      fin.open(cnam, ios::in);
      if (!fin.is_open()) {
        throw std::runtime_error("Path file for type " + std::string(type) +
                                 " does not exist!");
      }
    }
    fin.getline(nam, 256);
    fin.close();
  } else if (eflag) {
    strcpy(cnam, "path_");
    strcat(cnam, type);
    strcat(cnam, "_");
    strcat(cnam, name);
    strcat(cnam, ".");
    strcat(cnam, ch);
    fin.open(cnam, ios::in);
    if (!fin.is_open()) {
      fin.clear();
      strcpy(cnam, "path_");
      strcat(cnam, type);
      strcat(cnam, "_");
      strcat(cnam, name);
      fin.open(cnam, ios::in);
      if (!fin.is_open()) {
        fin.clear();
        strcpy(cnam, "path_");
        strcat(cnam, type);
        fin.open(cnam, ios::in);
        if (!fin.is_open()) {
          fin.clear();
          strcpy(cnam, "path");
          fin.open(cnam, ios::in);
          if (!fin.is_open()) {
            throw std::runtime_error("Path file for type " + std::string(type) +
                                     " does not exist!");
          }
        }
      }
    }
    fin.getline(nam, 256);
    fin.close();
  } else {
    strcpy(nam, path);
  }

  strcat(nam, type);
  strcat(nam, "_");
  strcat(nam, name);
  strcat(nam, ".");
  strcat(nam, ch);
}

ifstream *FBase::get_Istr(const char *a, ios::openmode mode) {
  char cnam[max_str];
  get_pathx(cnam, a);
  ifstream *pfin = new ifstream(cnam, mode);
  if (pfin->is_open())
    return (pfin);
  else {
    throw std::runtime_error("Error: " + std::string(cnam) +
                             " failed to open!");
  }
}

ofstream *FBase::get_Ostr(const char *a, ios::openmode mode) {
  char cnam[max_str];
  get_pathx(cnam, a);
  ofstream *pfout = new ofstream(cnam, mode);
  if (pfout->is_open())
    return (pfout);
  else {
    throw std::runtime_error("Error: " + std::string(cnam) +
                             " failed to open!");
  }
}

fstream *FBase::get_Fstr(const char *a, ios::openmode mode) {
  char cnam[max_str];
  get_pathx(cnam, a);
  fstream *pfstr = new fstream(cnam, mode);
  if (pfstr->is_open())
    return (pfstr);
  else {
    throw std::runtime_error("Error: " + std::string(cnam) +
                             " failed to open!");
  }
}

void FBase::dst_Istr(ifstream *pfin) {
  if (!pfin)
    return;
  if (!pfin->is_open()) {
    throw std::runtime_error("File not open");
  }
  delete pfin;
}

void FBase::dst_Ostr(ofstream *pfout) {
  if (!pfout)
    return;
  if (!pfout->is_open()) {
    throw std::runtime_error("File not open");
  }
  delete pfout;
}

void FBase::dst_Fstr(fstream *pfstr) {
  if (!pfstr)
    return;
  if (!pfstr->is_open()) {
    throw std::runtime_error("File not open");
  }
  delete pfstr;
}

long FBase::get_Fsiz(const char *a) {
  if (!Exists(a))
    return (0);
  int fld;
  struct stat datf;
  char cnam[max_str];
  get_pathx(cnam, a);
#ifdef _WIN32
  fld = _open(cnam, O_RDONLY);
#else
  fld = ::open(cnam, O_RDONLY);
#endif
  if (fld <= 0) {
    throw std::runtime_error(std::string(cnam) + " failed to open!");
  }
  if (fstat(fld, &datf)) {
    throw std::runtime_error(std::string(cnam) +
                             " failed on size determination");
  }
  ::close(fld);
  return (datf.st_size);
}

int FBase::Exists(const char *a) {
  char cnam[max_str];
  get_pathx(cnam, a);
  ifstream fin(cnam, ios::in);
  if (fin.is_open()) {
    fin.close();
    return (1);
  } else
    return (0);
}

char *FBase::get_Read(const char *a) {
  int fld;
  struct stat datf;
  char cnam[max_str];
  get_pathx(cnam, a);
#ifdef _WIN32
  fld = _open(cnam, O_RDONLY);
#else
  fld = ::open(cnam, O_RDONLY);
#endif
  if (fld <= 0) {
    throw std::runtime_error(std::string(cnam) + " failed to open");
  }
  if (fstat(fld, &datf)) {
    throw std::runtime_error(std::string(cnam) +
                             " failed on size determination");
  }
  ::close(fld);
  char *ptr = new char[datf.st_size];
  ifstream fin(cnam, ios::in);
  if (!fin.is_open()) {
    throw std::runtime_error(std::string(cnam) + " failed to open");
  }
  fin.read(ptr, datf.st_size);
  return (ptr);
}

char *FBase::get_Mmap(const char *a) {
  int fld;
  struct stat datf;
  char cnam[max_str];
  get_pathx(cnam, a);
#ifdef _WIN32
  // Windows-specific code for memory mapping
  fld = ::open(cnam, O_RDONLY);
  if (fld <= 0) {
    throw std::runtime_error(std::string(cnam) + " failed to open!");
  }
  if (fstat(fld, &datf)) {
    throw std::runtime_error(std::string(cnam) +
                             " failed on size determination");
  }
  HANDLE hFile = (HANDLE)_get_osfhandle(fld);

  HANDLE hMapFile =
      CreateFileMapping(hFile, NULL, PAGE_READONLY, DWORD_HI(datf.st_size),
                        DWORD_LO(datf.st_size), NULL);
  if (hMapFile == NULL) {
    throw std::runtime_error(std::string(cnam) + " failed to map");
  }

  char *ptr =
      (char *)MapViewOfFile(hMapFile, FILE_MAP_COPY, 0, 0, datf.st_size);
  if (ptr == NULL) {
    CloseHandle(hMapFile);
    throw std::runtime_error(std::string(cnam) + " failed to map");
  }

#else
  fld = ::open(cnam, O_RDONLY);
  if (fld <= 0) {
    throw std::runtime_error(std::string(cnam) + " failed to open");
  }
  if (fstat(fld, &datf)) {
    throw std::runtime_error(std::string(cnam) +
                             " failed on size determination");
  }
  char *ptr = (char *)mmap(0, datf.st_size, PROT_READ,
                           MAP_PRIVATE | MAP_NORESERVE, fld, 0);
  if (ptr == MAP_FAILED) {
    throw std::runtime_error(std::string(cnam) + " failed to map");
  }
  ::close(fld);
#endif
  return (ptr);
}

void FBase::dst_Mmap(const char *a, char *&ptr) {
  struct stat datf;
  char cnam[max_str];
  if (ptr == NULL) {
    cout << "NULL pointer" << endl;
    return;
  }
  get_pathx(cnam, a);
  if (stat(cnam, &datf)) {
    throw std::runtime_error(std::string(cnam) +
                             " failed on size determination");
  }

#ifdef _WIN32
  if (UnmapViewOfFile(ptr) == 0) {
    throw std::runtime_error(std::string(cnam) +
                             " failed to unmap view of file");
  }
#else
  if (munmap(ptr, datf.st_size)) {
    throw std::runtime_error(std::string(cnam) + " failed to unmap");
  }
#endif
  ptr = NULL;
}

void FBase::bin_Writ(const char *a, long nm, char *ptr) {
  ofstream *pfout = get_Ostr(a, ios::out);
  long k = 100000, i = 0;
  while (i + k < nm) {
    pfout->write((char *)ptr, k);
    i += k;
    ptr = ptr + k;
  }
  pfout->write((char *)ptr, nm - i);
  pfout->close();
  delete pfout;
}

int FBase::Gcom(int sflag) {
  if ((cflag & sflag) && !(oflag & sflag)) {
    oflag = oflag | sflag;
    return (1);
  } else
    return (0);
}

int FBase::Rcom(int sflag) {
  if ((cflag & sflag) && (oflag & sflag)) {
    oflag = oflag & (~sflag);
    return (1);
  } else
    return (0);
}

} // namespace iret
