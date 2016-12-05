package com.yefeng.multichannelpackage;

import android.content.Context;
import android.content.pm.ApplicationInfo;

import java.io.IOException;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

/**
 * Created by ponyets on 14-7-30.
 */
public final class ChannelReader {
    public static final String KEY_CHANNEL = "channel";
    public static final String KEY_SUB_CHANNEL = "subchannel";

    private ChannelReader() {
    }

    /**
     * 根据key,查找META-INF/路径下,文件名以key_开始的文件,读取文件名中携带的信息
     *
     * @param context
     * @param key
     * @return key所对应的value, 如找不到, 返回null
     */
    public static String getMETAInfo(Context context, String key) {
        String prefix = "META-INF/" + key + "_";
        ApplicationInfo appinfo = context.getApplicationInfo();
        // 取得APK安装的路径
        String sourceDir = appinfo.sourceDir;
        ZipFile zipfile = null;
        try {
            zipfile = new ZipFile(sourceDir);
            Enumeration<? extends ZipEntry> entries = zipfile.entries();
            // 遍历APK的所有文件,匹配路径以META-INF/${key}_开始的文件
            while (entries.hasMoreElements()) {
                ZipEntry entry = entries.nextElement();
                String entryName = entry.getName();
                if (entryName.startsWith(prefix)) {
                    // 截取下划线后的内容返回,便是key对应的value
                    return entryName.substring(prefix.length());
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (zipfile != null) {
                try {
                    zipfile.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return null;
    }

    /**
     * 读取META-INF/路径下存放的渠道信息
     *
     * @param context
     * @return 渠道信息, 找不到返回null
     */
    public static String getChannel(Context context) {
        return getMETAInfo(context, KEY_CHANNEL);
    }

    /**
     * 读取META-INF/路径下存放的子渠道信息
     *
     * @param context
     * @return 子渠道信息, 找不到返回null
     */
    public static String getSubChannel(Context context) {
        return getMETAInfo(context, KEY_SUB_CHANNEL);
    }
}
