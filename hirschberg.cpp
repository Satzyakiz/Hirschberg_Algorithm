
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <math.h>
#include <random>
#include <thread>
#include <chrono>

using namespace std;

class EditDistance
{
  string s1;
  string s2;
  bool is_reverse;

public:
  EditDistance(string *s1, string *s2)
  {
    if (s1->size() <= s2->size())
    {
      this->s1 = *s1;
      this->s2 = *s2;
      is_reverse = false;
    }
    else
    {
      this->s1 = *s2;
      this->s2 = *s1;
      is_reverse = true;
    }
  }

  /**************************************************************************************************/
  /*                                      2D-DP Implementation                                      */
  /**************************************************************************************************/
  pair<string, string> GetNeedlemanWunschAlignment(int ii, int jj, int ip, int jp)
  {
    int m = ip - ii;
    int n = jp - jj;
    vector<vector<int>> dp(n + 1, vector<int>(m + 1));
    for (int i = 0; i <= n; i++)
    {
      for (int j = 0; j <= m; j++)
      {
        if (i == 0 && j == 0)
        {
          dp[i][j] = 0;
        }
        else if (i > 0 && j == 0)
        {
          dp[i][j] = dp[i - 1][j] + 1;
        }
        else if (i == 0 && j > 0)
        {
          dp[i][j] = dp[i][j - 1] + 1;
        }
        else
        {
          int cost = (s1[ii + j - 1] == s2[jj + i - 1]) ? 0 : 1;
          dp[i][j] = min(1 + min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1] + cost);
        }
      }
    }

    int i = n, j = m;
    string seq1 = "", seq2 = "";
    while (i > 0 || j > 0)
    {
      if (i > 0 && dp[i - 1][j] + 1 == dp[i][j])
      {
        seq1 += '-';
        seq2 += s2[jj + i - 1];
        i--;
      }
      else if (j > 0 && dp[i][j - 1] + 1 == dp[i][j])
      {
        seq1 += s1[ii + j - 1];
        seq2 += '-';
        j--;
      }
      else
      {
        seq1 += s1[ii + j - 1];
        seq2 += s2[jj + i - 1];
        i--;
        j--;
      }
    }
    reverse(seq1.begin(), seq1.end());
    reverse(seq2.begin(), seq2.end());
    return make_pair(seq1, seq2);
  }

  pair<string, string> GetNeedlemanWunschAlignment()
  {
    pair<string, string> seq = GetNeedlemanWunschAlignment(0, 0, s1.size(), s2.size());
    if (is_reverse)
    {
      return make_pair(seq.second, seq.first);
    }
    return seq;
  }

  /**************************************************************************************************/
  /*                                    Hirschberg Implementation                                    */
  /**************************************************************************************************/
  vector<int> GetReversed1dDpLastRow(int ii, int ip, int jj, int jp)
  {
    int len1 = ip - ii;
    int len2 = jp - jj;
    vector<vector<int>> dp(2, vector<int>(len1 + 1, 0));
    int curridx = 0;
    for (int i = 0; i <= len2; i++)
    {
      for (int j = 0; j <= len1; j++)
      {
        if (i == 0 && j == 0)
        {
          dp[curridx][j] = 0;
        }
        else if (i > 0 && j == 0)
        {
          dp[curridx][j] = dp[1 - curridx][j] + 1;
        }
        else if (i == 0 && j > 0)
        {
          dp[curridx][j] = dp[curridx][j - 1] + 1;
        }
        else
        {
          int cost = (s1[ip - j] == s2[jp - i]) ? 0 : 1;
          dp[curridx][j] = min(dp[1 - curridx][j] + 1, min(dp[curridx][j - 1] + 1, dp[1 - curridx][j - 1] + cost));
        }
      }
      curridx = 1 - curridx;
    }
    return dp[1 - curridx];
  }

  vector<int> Get1dDpLastRow(int ii, int ip, int jj, int jp)
  {
    int len1 = ip - ii;
    int len2 = jp - jj;
    vector<vector<int>> dp(2, vector<int>(len1 + 1, 0));
    int curridx = 0;
    for (int i = 0; i <= len2; i++)
    {
      for (int j = 0; j <= len1; j++)
      {
        if (i == 0 && j == 0)
        {
          dp[curridx][j] = 0;
        }
        else if (i > 0 && j == 0)
        {
          dp[curridx][j] = dp[1 - curridx][j] + 1;
        }
        else if (i == 0 && j > 0)
        {
          dp[curridx][j] = dp[curridx][j - 1] + 1;
        }
        else
        {
          int cost = (s1[ii + j - 1] == s2[jj + i - 1]) ? 0 : 1;
          dp[curridx][j] = min(dp[1 - curridx][j] + 1, min(dp[curridx][j - 1] + 1, dp[1 - curridx][j - 1] + cost));
        }
      }
      curridx = 1 - curridx;
    }
    return dp[1 - curridx];
  }

  pair<string, string> HirschbergHelper(int i, int j, int ip, int jp)
  {
    if (jp - j == 1)
    {
      return GetNeedlemanWunschAlignment(i, j, ip, jp);
    }
    if (jp <= j)
    {
      return make_pair("", "");
    }
    int mid = (j + jp) / 2;
    string S1 = s1.substr(i, ip - i), S2 = s2.substr(j, mid - j), S3 = s2.substr(mid, jp - mid);
    vector<int> prefix = Get1dDpLastRow(i, ip, j, mid);
    vector<int> suffix = GetReversed1dDpLastRow(i, ip, mid, jp);
    int maxidx = -1;
    int minweight = -1;
    for (int idx = 0; idx < prefix.size(); idx++)
    {
      int weight = prefix[idx] + suffix[suffix.size() - idx - 1];
      if (maxidx == -1 || minweight >= weight)
      {
        maxidx = idx;
        minweight = weight;
      }
    }
    pair<string, string> seq1 = HirschbergHelper(i, j, maxidx + i, mid);
    pair<string, string> seq2 = HirschbergHelper(maxidx + i, mid, ip, jp);
    return make_pair(seq1.first + seq2.first, seq1.second + seq2.second);
  }

  pair<string, string> GetHirschbergAlignment()
  {
    pair<string, string> seq = HirschbergHelper(0, 0, s1.length(), s2.length());
    if (is_reverse)
    {
      return make_pair(seq.second, seq.first);
    }
    return seq;
  }
};

/**************************************************************************************************/
/*                                           Unit Tests                                           */
/**************************************************************************************************/
mt19937 random_generator(chrono::steady_clock::now().time_since_epoch().count());
uniform_int_distribution<int> character_distribution('a', 'z');

void UnitTest()
{
  bool all_passed = true;
  uniform_int_distribution<int> length_distribution(1, 100);
  for (int t = 0; t < 100000; t++)
  {
    string X = "", Y = "";
    int n = length_distribution(random_generator);
    for (int i = 0; i < n; i++)
    {
      X += character_distribution(random_generator);
    }
    int m = length_distribution(random_generator);
    for (int i = 0; i < m; i++)
    {
      Y += character_distribution(random_generator);
    }
    EditDistance ed(&X, &Y);
    pair<string, string> seq1 = ed.GetHirschbergAlignment();
    pair<string, string> seq2 = ed.GetNeedlemanWunschAlignment();
    int cost1 = 0;
    bool wrong_alignment = false;
    int original_x = 0, original_y = 0;
    for (int i = 0; i < seq1.first.size(); i++)
    {
      if (seq1.first[i] == '-' && seq1.second[i] == '-')
      {
        wrong_alignment = true;
        break;
      }
      if (seq1.first[i] != '-')
      {
        if (seq1.first[i] != X[original_x])
        {
          wrong_alignment = true;
          break;
        }
        original_x++;
      }
      if (seq1.second[i] != '-')
      {
        if (seq1.second[i] != Y[original_y])
        {
          wrong_alignment = true;
          break;
        }
        original_y++;
      }
      if (seq1.first[i] != seq1.second[i])
      {
        cost1++;
      }
    }
    int cost2 = 0;
    for (int i = 0; i < seq2.first.size(); i++)
    {
      if (seq2.first[i] != seq2.second[i])
      {
        cost2++;
      }
    }
    if (wrong_alignment || cost1 != cost2)
    {
      cout << "Wrong Alignment" << endl;
      cout << "X: " << X << endl;
      cout << "Y: " << Y << endl;
      cout << "Hirschberg's Output" << endl;
      cout << seq1.first << endl
           << seq1.second << endl;
      cout << "Needleman-Wunschs Output" << endl;
      cout << seq2.first << endl
           << seq2.second << endl
           << endl;
      all_passed = false;
    }
  }
  if (all_passed)
  {
    cout << "All test cases passed" << endl;
  }
}

/**************************************************************************************************/
/*                                       Performance Tests                                        */
/**************************************************************************************************/
float CpuUserTimeDifference(rusage start, rusage end)
{
  return (end.ru_utime.tv_sec - start.ru_utime.tv_sec) + ((float)(end.ru_utime.tv_usec - start.ru_utime.tv_usec)) / 1000000;
}

float CpuSystemTimeDifference(rusage start, rusage end)
{
  return (end.ru_stime.tv_sec - start.ru_stime.tv_sec) + ((float)(end.ru_stime.tv_usec - start.ru_stime.tv_usec)) / 1000000;
}

string GenerateText(int len)
{
  string s = "";
  for (int i = 0; i < len; i++)
  {
    s += (char)character_distribution(random_generator);
  }
  return s;
}

pair<string, string> RunHirschbergPerfTest(string &s1, string &s2)
{
  EditDistance ed(&s1, &s2);
  rusage start, end;
  struct timespec t1, t2;
  getrusage(RUSAGE_SELF, &start);
  clock_gettime(CLOCK_MONOTONIC, &t1);
  pair<string, string> res = ed.GetHirschbergAlignment();
  clock_gettime(CLOCK_MONOTONIC, &t2);
  getrusage(RUSAGE_SELF, &end);
  double mem_usage_mb = (double)end.ru_maxrss / 1000.0;
  cout << "Memory usage: " << mem_usage_mb << " MB" << endl;
  cout << "CPU time (system) used: " << CpuSystemTimeDifference(start, end) << " seconds" << endl;
  cout << "CPU time (user) used: " << CpuUserTimeDifference(start, end) << " seconds" << endl;
  cout << "Elapsed time: " << (t2.tv_sec - t1.tv_sec) + ((float)(t2.tv_nsec - t1.tv_nsec)) / 1000000000 << " seconds" << endl;
  return res;
}

pair<string, string> RunNeedlemanWunschPerfTest(string &s1, string &s2)
{
  EditDistance ed(&s1, &s2);
  rusage start, end;
  struct timespec t1, t2;
  getrusage(RUSAGE_SELF, &start);
  clock_gettime(CLOCK_MONOTONIC, &t1);
  pair<string, string> res = ed.GetNeedlemanWunschAlignment();
  clock_gettime(CLOCK_MONOTONIC, &t2);
  getrusage(RUSAGE_SELF, &end);
  double mem_usage_mb = (double)end.ru_maxrss / 1000.0;
  cout << "Memory usage: " << mem_usage_mb << " MB" << endl;
  cout << "CPU time (system) used: " << CpuSystemTimeDifference(start, end) << " seconds" << endl;
  cout << "CPU time (user) used: " << CpuUserTimeDifference(start, end) << " seconds" << endl;
  cout << "Elapsed time: " << (t2.tv_sec - t1.tv_sec) + ((float)(t2.tv_nsec - t1.tv_nsec)) / 1000000000 << " seconds" << endl;
  return res;
}

int main(int argc, char *argv[])
{
  if ((string)argv[1] == "unit-test")
  {
    UnitTest();
  }
  else if ((string)argv[2] == "--file")
  {
    ifstream infile1(argv[3]);
    ifstream infile2(argv[4]);
    string s1, s2;
    infile1 >> s1;
    infile2 >> s2;
    pair<string, string> res;
    if ((string)argv[1] == "hirschberg")
    {
      res = RunHirschbergPerfTest(s1, s2);
    }
    else if ((string)argv[1] == "needleman-wunsch")
    {
      res = RunNeedlemanWunschPerfTest(s1, s2);
    }
    infile1.close();
    infile2.close();
    ofstream outfile("output.txt");
    outfile << res.first << endl;
    outfile << res.second << endl;
  }
  else if ((string)argv[2] == "--length")
  {
    int len1 = stoi(argv[3]);
    int len2 = stoi(argv[4]);
    string s1 = GenerateText(len1);
    string s2 = GenerateText(len2);
    pair<string, string> res;
    if ((string)argv[1] == "hirschberg")
    {
      res = RunHirschbergPerfTest(s1, s2);
    }
    else if ((string)argv[1] == "needleman-wunsch")
    {
      res = RunNeedlemanWunschPerfTest(s1, s2);
    }
    ofstream outfile("output.txt");
    outfile << res.first << endl;
    outfile << res.second << endl;
  }
  else
  {
    string s1 = argv[2];
    string s2 = argv[3];
    EditDistance ed(&s1, &s2);
    pair<string, string> res;
    if ((string)argv[1] == "hirschberg")
    {
      res = RunHirschbergPerfTest(s1, s2);
    }
    else if ((string)argv[1] == "needleman-wunsch")
    {
      res = RunNeedlemanWunschPerfTest(s1, s2);
    }
    cout << res.first << endl;
    cout << res.second << endl;
  }
  return 0;
}
