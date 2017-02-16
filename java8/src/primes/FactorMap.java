package primes;

import java.util.*;
import java.util.function.BiConsumer;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.stream.Stream;

/**
 * Created by gcharles on 2/14/17.
 */
public class FactorMap {
    private final Map<Integer, Integer> internal = new TreeMap<>();

    public static FactorMap factor(long number) {
        PrimeSupplier primes = new PrimeSupplier();
        long residual = number;

        FactorMap fm = new FactorMap();

        for (int n = primes.getAsInt(); n * n <= residual; n = primes.getAsInt()) {
            //int n = primes.getAsInt();
            while (residual % n == 0) {
                fm.internal.merge(n, 1, (oldV, newV) -> oldV + 1);
                residual /= n;
            }
        }

        if (residual > 1) {
            fm.internal.merge((int)residual, 1, (oldV, newV) -> oldV + 1);
        }

        return fm;
    }

    public static void main(String[] args) {
        System.out.println(FactorMap.factor(28));
        System.out.println(FactorMap.factor(76564125).factorCount());
    }

    @Override
    public String toString() {
        return internal.toString();
    }

    public int factorCount() {
        return internal.values().stream().reduce(1, (prod, val) -> prod * (val + 1));
    }

    public boolean isEmpty() {
        return internal.isEmpty();
    }

    public Integer getExponentFor(Integer factor) {
        return internal.get(factor);
    }

    public boolean containsFactor(Integer factor) {
        return internal.containsKey(factor);
    }

    public Set<Integer> factors() {
        return internal.keySet();
    }

    public Set<Map.Entry<Integer, Integer>> entries() {
        return internal.entrySet();
    }
//
//    @Override
//    public boolean containsValue(Object value) {
//        return internal.containsValue(value);
//    }
//
//    @Override
//    public Integer get(Object key) {
//        return internal.get(key);
//    }
//
//    @Override
//    public Integer put(Integer key, Integer value) {
//        return internal.put(key, value);
//    }
//
//    @Override
//    public Integer remove(Object key) {
//        return internal.remove(key);
//    }
//
//    @Override
//    public void putAll(Map<? extends Integer, ? extends Integer> m) {
//        internal.putAll(m);
//    }
//
//    @Override
//    public void clear() {
//        internal.clear();
//    }
//
//    @Override
//    public Set<Integer> keySet() {
//        return internal.keySet();
//    }
//
//    @Override
//    public Collection<Integer> values() {
//        return internal.values();
//    }
//
//    @Override
//    public Set<Entry<Integer, Integer>> entrySet() {
//        return internal.entrySet();
//    }
//
//    @Override
//    public boolean equals(Object o) {
//        return internal.equals(o);
//    }
//
//    @Override
//    public int hashCode() {
//        return internal.hashCode();
//    }
//
//    @Override
//    public Integer getOrDefault(Object key, Integer defaultValue) {
//        return internal.getOrDefault(key, defaultValue);
//    }
//
//    @Override
//    public void forEach(BiConsumer<? super Integer, ? super Integer> action) {
//        internal.forEach(action);
//    }
//
//    @Override
//    public void replaceAll(BiFunction<? super Integer, ? super Integer, ? extends Integer> function) {
//        internal.replaceAll(function);
//    }
//
//    @Override
//    public Integer putIfAbsent(Integer key, Integer value) {
//        return internal.putIfAbsent(key, value);
//    }
//
//    @Override
//    public boolean remove(Object key, Object value) {
//        return internal.remove(key, value);
//    }
//
//    @Override
//    public boolean replace(Integer key, Integer oldValue, Integer newValue) {
//        return internal.replace(key, oldValue, newValue);
//    }
//
//    @Override
//    public Integer replace(Integer key, Integer value) {
//        return internal.replace(key, value);
//    }
//
//    @Override
//    public Integer computeIfAbsent(Integer key, Function<? super Integer, ? extends Integer> mappingFunction) {
//        return internal.computeIfAbsent(key, mappingFunction);
//    }
//
//    @Override
//    public Integer computeIfPresent(Integer key, BiFunction<? super Integer, ? super Integer, ? extends Integer> remappingFunction) {
//        return internal.computeIfPresent(key, remappingFunction);
//    }
//
//    @Override
//    public Integer compute(Integer key, BiFunction<? super Integer, ? super Integer, ? extends Integer> remappingFunction) {
//        return internal.compute(key, remappingFunction);
//    }
//
//    @Override
//    public Integer merge(Integer key, Integer value, BiFunction<? super Integer, ? super Integer, ? extends Integer> remappingFunction) {
//        return internal.merge(key, value, remappingFunction);
//    }
}
